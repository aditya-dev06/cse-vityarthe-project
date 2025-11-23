import time

class HospitalManager:
    def __init__(self):
        # We use a dictionary to store patients for fast lookups
        # Format: {ID: {'name': 'Name', 'age': 30, 'disease': 'Flu'}}
        self.patients = {}

    def admit_patient(self):
        print("\n--- Admit New Patient ---")
        p_id = input("Enter Patient ID (unique): ")
        
        # Check if ID already exists
        if p_id in self.patients:
            print("Error: A patient with this ID already exists.")
            return

        name = input("Enter Patient Name: ")
        age = input("Enter Patient Age: ")
        disease = input("Enter Disease/Reason for visit: ")
        date = time.strftime("%d/%m/%Y") # Auto-generate today's date

        # Saving the data
        self.patients[p_id] = {
            'name': name,
            'age': age,
            'disease': disease,
            'date': date
        }
        print(f"Success: Patient {name} admitted successfully!")

    def view_patients(self):
        print("\n--- List of Admitted Patients ---")
        if not self.patients:
            print("No patients currently admitted.")
        else:
            print(f"{'ID':<10} {'Name':<20} {'Age':<5} {'Disease':<20} {'Date':<12}")
            print("-" * 70)
            for p_id, details in self.patients.items():
                print(f"{p_id:<10} {details['name']:<20} {details['age']:<5} {details['disease']:<20} {details['date']:<12}")

    def search_patient(self):
        print("\n--- Search Patient ---")
        p_id = input("Enter Patient ID to search: ")
        
        if p_id in self.patients:
            p = self.patients[p_id]
            print("\nPatient Found!")
            print(f"Name: {p['name']}")
            print(f"Age: {p['age']}")
            print(f"Disease: {p['disease']}")
            print(f"Admit Date: {p['date']}")
        else:
            print("Patient not found.")

    def discharge_patient(self):
        print("\n--- Discharge Patient ---")
        p_id = input("Enter Patient ID to discharge: ")
        
        if p_id in self.patients:
            removed_patient = self.patients.pop(p_id)
            print(f"Success: Patient {removed_patient['name']} has been discharged.")
        else:
            print("Error: Patient ID not found.")

# --- Main Execution ---
def main():
    system = HospitalManager()
    
    while True:
        print("\n=== HOSPITAL MANAGEMENT SYSTEM ===")
        print("1. Admit Patient")
        print("2. View All Patients")
        print("3. Search Patient Details")
        print("4. Discharge Patient")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            system.admit_patient()
        elif choice == '2':
            system.view_patients()
        elif choice == '3':
            system.search_patient()
        elif choice == '4':
            system.discharge_patient()
        elif choice == '5':
            print("Exiting system. Stay healthy!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
