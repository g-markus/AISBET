<scenario>
# The task relates to the following initial situation:

A large hospital system, "City Hospital Group," manages patient appointments, medical records, and billing across multiple hospitals and clinics. They are implementing a new electronic health record (EHR) system to streamline these processes and improve patient care.
</scenario>

<problem>
# 1. Task (25 points)

The EHR system needs to be able to efficiently search for patients based on various criteria, including their medical record number (MRN), last name, and date of birth. Due to privacy regulations, access to specific patient records should be restricted to authorized personnel based on their roles (e.g., doctor, nurse, administrator).  Develop a search function that accounts for both efficiency and access control.
</problem>

<data_elements>
## Patient Record Class

@startuml
class PatientRecord {
- mrn : Integer
- lastName : String
- dateOfBirth : Date
- medicalHistory : String
...
}
@enduml

Public getter methods (e.g., `getMrn()`, `getLastName()`, `getDateOfBirth()`, `getMedicalHistory()`) are available for each attribute.

## User Class

@startuml
class User {
- userId : Integer
- role : String 
...
}
@enduml

Public getter methods (e.g., `getUserId()`, `getRole()`) are available for each attribute.


The patient records are stored in a hash table `patientRecords` where the key is the MRN (Integer) and the value is the `PatientRecord` object.  Assume a suitable hash table implementation exists with methods like  `put(key, value)`, `get(key)`, `containsKey(key)`, and `size()`.


The user roles and their corresponding access permissions are defined as follows:

* "doctor": Can access all patient data.
* "nurse": Can access patient demographics (MRN, last name, date of birth) but not the full medical history.
* "administrator": Can access only the MRN and last name.

Input search criteria will be provided as a string `searchString` which can be either an MRN (numeric string), a last name, or a date of birth (formatted as "YYYY-MM-DD"). The currently logged-in user will be provided as a `User` object.

The output should be a string containing the accessible information for the matching patient record(s), or an appropriate message if no match is found or the user does not have access.
</data_elements>

<pseudocode_task>
Create a function `searchPatients(patientRecords: HashTable, searchString: String, currentUser: User): String` that performs the following actions:

* Searches the `patientRecords` for matching patient(s) based on the provided `searchString`. The search should handle matches by MRN, last name, or date of birth.
* Filters the returned information based on the `currentUser`'s role and access permissions.
* Returns a string containing the accessible information of the found patient(s) or an appropriate message if no match is found or if access is denied.  Format the output clearly, indicating which fields are included.

Do not implement specific hash table operations or string parsing details.  Focus on the high-level logic of searching, filtering based on user role, and formatting the output.
</pseudocode_task>