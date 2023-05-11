## FDO Manager (API)

The FDO manager API have multiple models (or database tables) which are :
* FDO : which is the table that contains the whole FDO input.
* profiles : which contains profiles information (attributes definition is still on progress, therefore the current one is general)
* PID_metadata : which contains metadata of the data or artifact .
* artifact_prop : which contains an artifact information (which is also linked to each input metadata).
* PID_records : which contains metadata information and profiles history.  


Currently the available API calls are : 

* FDO 
  - GET `http://127.0.0.1:8000/getfdo/`
  - POST `http://127.0.0.1:8000/addfdo/`
* Profiles 
  * GET `http://127.0.0.1:8000/getprofile/`
  * POST `http://127.0.0.1:8000/addprofile/`
* Metadata
  * GET `http://127.0.0.1:8000/getmetadata/`
  * POST `http://127.0.0.1:8000/addmetadata/`
* Records
  * GET `http://127.0.0.1:8000/getrecord/`
  * post `http://127.0.0.1:8000/addrecord/`
* Artifact property
  * GET ``
  * POST ``
* 
