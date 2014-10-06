# bank\_sort\_code

Adds a `sort_code` field to `res.partner.bank` in Odoo.

## Known limitations

* This may also need to be put on `res.bank`
* We haven't yet investigated what impact putting the sort code in `sort_code`
  field instead of in existing fields might have on other modules dependent on it.
