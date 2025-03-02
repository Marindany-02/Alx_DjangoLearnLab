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

## Security Features Implemented

1. **Secure Settings:**
   - Disabled DEBUG in production.
   - Added XSS, Content Type Sniffing, and Frame protection headers.
   - Enforced secure cookies.

2. **CSRF Protection:**
   - CSRF tokens added to all forms.

3. **SQL Injection Prevention:**
   - Used Django ORM with safe input handling (no raw SQL).

4. **Content Security Policy (CSP):**
   - Add django-csp middleware or manual headers for CSP control.

5. **Access Control:**
   - Permissions enforced with decorators.

Test with different users to verify access restrictions