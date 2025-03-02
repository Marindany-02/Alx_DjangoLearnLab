Introduction to Django
# Django Permissions and Groups Setup

## Custom Permissions:
- can_view: View book records
- can_create: Create new book records
- can_edit: Edit existing book records
- can_delete: Delete book records

## Groups:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: Full CRUD (can_view, can_create, can_edit, can_delete)

## Testing:
1. Create test users and assign them to groups via the Django admin.
2. Log in as different users and attempt various actions to verify permission enforcement.