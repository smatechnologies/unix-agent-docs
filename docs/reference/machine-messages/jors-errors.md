# JORS/FTServer Errors

The UNIXLSAM.log file contains these errors:

* **Unable to open master socket (return : return errno : errno)**
* **Select on master socket failed (errmo : errno)**
* **Accept on master socket failed (errno : errno)**
* **Could not set buffer size**

**Origination**: FTServer

* The communications channel could not be initialized.
* The return and errno fields provide the specific reason.

---

* **fork() failed (errno : errno)**	

**Origination**:FTServer

* A child process to handle the JORS/FTServer duties could not be spawned.
* The errno field provides the specific reason.