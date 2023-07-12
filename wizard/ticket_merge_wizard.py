from odoo import api, fields, models

class TicketMergeWizard(models.TransientModel):
    _name = 'ticket.merge.wizard'
    _description = 'Wizard to merge tickets'

    ticket_ids = fields.Many2many('helpdesk.ticket', string='Tickets to Merge')

    def merge_tickets(self):
        self.ensure_one()
        # You might want to implement a more sophisticated merging logic
        main_ticket = self.ticket_ids[0]
        for ticket in self.ticket_ids[1:]:
            main_ticket.description += "\n\n" + ticket.description
            ticket.unlink()
        return {}