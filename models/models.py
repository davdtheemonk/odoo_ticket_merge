from odoo import models, fields, api
from odoo.exceptions import UserError
class TicketMergeWizard(models.TransientModel):
    _name = 'ticket.merge.wizard'
    _description = 'Ticket Merge Wizard'
    
    main_ticket_id = fields.Many2one('helpdesk.ticket', string='Main Ticket', required=True)
    secondary_ticket_ids = fields.Many2many('helpdesk.ticket', string='Secondary Tickets')

    def merge_tickets(self):
        main_ticket = self.main_ticket_id
        secondary_tickets = self.secondary_ticket_ids

        # Merge information from secondary tickets into the main ticket
        for secondary_ticket in secondary_tickets:
            if( main_ticket.partner_id != secondary_ticket.partner_id or
            main_ticket.user_id != secondary_ticket.user_id or
            main_ticket.team_id != secondary_ticket.team_id
            or
            main_ticket.stage_id != secondary_ticket.stage_id):
                raise UserError("Cannot merge tickets with different stage or partner or assigneds or contact.")
            
            main_ticket.name = main_ticket.name
            secondary_ticket.message_post(body='This ticket has been merged into another ticket.')
            secondary_ticket.unlink()

        # Optional: Update other fields as needed (e.g., priority, status, etc.)

        # Refresh the main ticket's display_name to reflect the changes
        main_ticket.invalidate_cache()

        return {'type': 'ir.actions.act_window_close'}
    
class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'
    _name = "ticket.helpdesk.in"

    merged_tickets = fields.Text(string='Merged Tickets', compute='_compute_merged_tickets')
    sla_ids = fields.Many2many(
    'helpdesk.sla',
    'ticket_helpdesk_in_sla_rel',
    'ticket_id',
    'sla_id',
)
    @api.depends('name', 'message_ids')
    def _compute_merged_tickets(self):
        for ticket in self:
            merged_ticket_names = []
            for message in ticket.message_ids.filtered(lambda msg: msg.subtype_id.internal):
                if 'merged into another ticket' in message.body:
                    merged_ticket_names.append(message.model)
            ticket.merged_tickets = '\n'.join(merged_ticket_names)