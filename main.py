from ocean import get_similar_companies
from prospeo import get_contacts
from brevo import send_emails

print("=" * 60)
print("AUTOMATED OUTREACH PIPELINE")
print("=" * 60)

domain = input("\nEnter Company Domain: ").strip()

# Stage 1
companies = get_similar_companies(domain)

if not companies:
    print("\nNo companies found.")
    exit()

print("\n[Stage 1 Results]")
for company in companies:
    print(f"- {company}")

# Stage 2
contacts = get_contacts(companies)

print("\n[Stage 2 Results]")

for contact in contacts:

    print(
        f"Company: {contact['company']} | "
        f"Name: {contact['name']} | "
        f"Email: {contact['email']}"
    )

# Filter emails
valid_contacts = []

for contact in contacts:

    email = contact["email"]

    if (
        email
        and email != "Not Available"
        and "@" in str(email)
    ):
        valid_contacts.append(contact)

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print(f"Companies Found      : {len(companies)}")
print(f"Contacts Found       : {len(contacts)}")
print(f"Valid Emails Found   : {len(valid_contacts)}")

choice = input("\nSend Emails? (Y/N): ")

if choice.upper() == "Y":

    if len(valid_contacts) == 0:
        print("\nNo valid emails available.")
    else:
        send_emails(valid_contacts)

else:
    print("\nEmail sending cancelled.")