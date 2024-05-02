class VisaIssuanceTracker:
    def __init__(self):
        self.issuance_records = {}
        self.issuance_statistics = {'total_issued': 0}

    def convertFileToDictionary(self):
        fileObj = open("fileDataStore.txt", "r")
        currList = eval(fileObj.read())["store"]
        fileObj.close()
        return currList
    
    def insertIntoFile(self, currList):
        fileObj = open("fileDataStore.txt", "w")
        obj = {"store": currList}
        fileObj.write(str(obj))
        fileObj.close()

    def isRecordPresentInDatabase(self, id):
        currList = self.convertFileToDictionary()
        result = [-1, None]
        index = 0
        for obj in currList:
            if obj['issuance_id'] == id:
                result[0] = index 
                result[1] = obj 
                break
            index += 1
        return result


    def create_issuance_record(self, issuance_id, visa_type, applicant_name, approval_date):
        # Create a new issuance record
        issuance_data = {
            'issuance_id': issuance_id,
            'visa_type': visa_type,
            'applicant_name': applicant_name,
            'approval_date': approval_date,
            'issuance_date': None  
        }
        #self.issuance_records[issuance_id] = issuance_data
        self.issuance_statistics['total_issued'] += 1
        currList = self.convertFileToDictionary()
        currList.append(issuance_data)
        self.insertIntoFile(currList)
        print("Issuance record created successfully.")

    def update_issuance_record(self, issuance_id, visa_type, applicant_name, approval_date, issuance_date):
        # Update issuance record with all parameters
        result = self.isRecordPresentInDatabase(issuance_id)
        print(result[0])
        print(result[1])
        if result[0] != -1:
            old_record = result[1]
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
                currList = self.convertFileToDictionary()
                currList.pop(result[0])
                currList.append(old_record)
                self.insertIntoFile(currList)
                print("Issuance record updated successfully.")
            else:
                print("No fields were updated. Old record values remain unchanged.")
        else:
            print("Issuance ID not found.")

    def delete_issuance_record(self, issuance_id):
        # Delete issuance record
        result = self.isRecordPresentInDatabase(issuance_id)
        if result[0] != -1:
            currList = self.convertFileToDictionary()
            currList.pop(result[0])
            self.insertIntoFile(currList)
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
        result = self.isRecordPresentInDatabase(issuance_id)
        if result[0] != -1:
            return result[1]
        else:
            print("Issuance record not found.")
            return None

    def display_issuance_records(self):
        # Display all issuance records
        print("\nIssuance Records:")
        currList = self.convertFileToDictionary()
        for data in currList:
            print("Issuance ID:", data['issuance_id'])
            print("Visa Type:", data['visa_type'])
            print("Applicant Name:", data['applicant_name'])
            print("Approval Date:", data['approval_date'])
            print("Issuance Date:", data['issuance_date'])
            print()

# Example Usage with User Input
tracker = VisaIssuanceTracker()

while True:
    print("\n\n*")
    print("\nChoose an option:")
    print("1. Create issuance record")
    print("2. Update issuance record")
    print("3. Delete issuance record")
    print("4. Report issuance statistics")
    print("5. Read issuance record")
    print("6. Display issuance records")
    print("7. Exit")

    choice = input("Enter your choice: ")
    print("\n\n*")



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
        result = tracker.isRecordPresentInDatabase(issuance_id)
        if result[0] != -1:
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
