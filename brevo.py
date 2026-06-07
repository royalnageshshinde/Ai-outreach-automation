def send_emails(contacts):
    
    print("\n[Stage 3] Brevo")
    print("-" * 40)

    count = 0

    for contact in contacts:

        print(
            f"To: {contact['email']} | "
            f"Name: {contact['name']} | "
            f"Company: {contact['company']}"
        )

        count += 1

    print("\n" + "-" * 40)
    print(f"✓ Total Emails Processed: {count}")