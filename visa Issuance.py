class VisaIssuanceTracker:
    def __init__(self):
        self.issuance_records = {}
        self.issuance_statistics = {'total_issued': 0}

    def create_issuance_record(self, issuance_id, visa_type, applicant_name, approval_date):
        # Create a new issuance record
        issuance_data = {
            'visa_type': visa_type,
            'applicant_name': applicant_name,
            'approval_date': approval_date,
            'issuance_date': None  # Issuance date will be updated later
        }
        self.issuance_records[issuance_id] = issuance_data
        print("Issuance record created successfully.")

    def update_issuance_record(self, issuance_id, visa_type, applicant_name, approval_date, issuance_date):
        # Update issuance record with all parameters
        if issuance_id in self.issuance_records:
            old_record = self.issuance_records[issuance_id]
            updated_fields = []

            if visa_type != "":
                updated_fields.append("Visa Type: " + old_record['visa_type'] + " -> " + visa_type)
                old_record['visa_type'] = visa_type

            if applicant_name != "":
                updated_fields.append("Applicant Name: " + old_record['applicant_name'] + " -> " + applicant_name)
                old_record['applicant_name'] = applicant_name

            if approval_date != "":
                updated_fields.append("Approval Date: " + old_record['approval_date'] + " -> " + approval_date)
                old_record['approval_date'] = approval_date

            if issuance_date != "":
                updated_fields.append("Issuance Date: " + str(old_record['issuance_date']) + " -> " + issuance_date)
                old_record['issuance_date'] = issuance_date

            if updated_fields:
                print("Old Record Values:")
                for field in updated_fields:
                    print(field)
                print("Issuance record updated successfully.")
            else:
                print("No fields were updated. Old record values remain unchanged.")
        else:
            print("Issuance ID not found.")

    def delete_issuance_record(self, issuance_id):
        # Delete issuance record
        if issuance_id in self.issuance_records:
            del self.issuance_records[issuance_id]
            # Update statistics
            self.issuance_statistics['total_issued'] -= 1
            print("Issuance record deleted successfully.")
        else:
            print("Issuance record not found.")

    def report_issuance_statistics(self):
        # Report issuance statistics
        print("\nVisa Issuance Statistics:")
        print("Total Issued Visas:", self.issuance_statistics['total_issued'])

    def read_issuance_record(self, issuance_id):
        # Read issuance record
        if issuance_id in self.issuance_records:
            return self.issuance_records[issuance_id]
        else:
            print("Issuance record not found.")
            return None

    def display_issuance_records(self):
        # Display all issuance records
        print("\nIssuance Records:")
        for issuance_id, data in self.issuance_records.items():
            print("Issuance ID:", issuance_id)
            print("Visa Type:", data['visa_type'])
            print("Applicant Name:", data['applicant_name'])
            print("Approval Date:", data['approval_date'])
            print("Issuance Date:", data['issuance_date'])
            print()

# Example Usage with User Input
tracker = VisaIssuanceTracker()

while True:
    print("\n\n**")
    print("\nChoose an option:")
    print("1. Create issuance record")
    print("2. Update issuance record")
    print("3. Delete issuance record")
    print("4. Report issuance statistics")
    print("5. Read issuance record")
    print("6. Display issuance records")
    print("7. Exit")

    choice = input("Enter your choice: ")
    print("\n\n**")


    if choice == '1':
        print("\nCreating Issuance Record:")
        issuance_id = int(input("Enter issuance ID: "))
        visa_type = input("Enter visa type: ")
        applicant_name = input("Enter applicant name: ")
        approval_date = input("Enter approval date (YYYY-MM-DD): ")
        tracker.create_issuance_record(issuance_id, visa_type, applicant_name, approval_date)
    elif choice == '2':
        print("\nUpdating Issuance Record:")
        issuance_id = int(input("Enter issuance ID to update: "))
        if issuance_id in tracker.issuance_records:
            visa_type = input("Enter new visa type : ")
            applicant_name = input("Enter new applicant name : ")
            approval_date = input("Enter new approval date (YYYY-MM-DD) : ")
            issuance_date = input("Enter new issuance date (YYYY-MM-DD) : ")
            tracker.update_issuance_record(issuance_id, visa_type, applicant_name, approval_date, issuance_date)
        else:
            print("Issuance ID not found.")
    elif choice == '3':
        print("\nDeleting Issuance Record:")
        issuance_id = int(input("Enter issuance ID to delete: "))
        tracker.delete_issuance_record(issuance_id)
    elif choice == '4':
        tracker.report_issuance_statistics()
    elif choice == '5':
        print("\nReading Issuance Record:")
        issuance_id = int(input("Enter issuance ID to read: "))
        record = tracker.read_issuance_record(issuance_id)
        if record:
            print("Issuance Record:")
            print("Issuance ID:", issuance_id)
            print("Visa Type:", record['visa_type'])
            print("Applicant Name:", record['applicant_name'])
            print("Approval Date:", record['approval_date'])
            print("Issuance Date:", record['issuance_date'])
    elif choice == '6':
        tracker.display_issuance_records()
    elif choice == '7':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
