# RTCAttachmentDownloader

## Requirements

* Download Python 3
* Create in C a folder called Python to install python 3
    * C:\Python
* install python 3 and choose custom/advanced install to select the folder created in the previous step.
* Pipenv  execute `prepare_environment.bat`
* active pulse VPN
* execute `start_rtc_attachement_downloader.bat`

## Configuration
* Configure properties in `properties\properties.py`
    * rtc_url = url of rtc, is configure by default, no need to change it
     
            rtc_url = https://rtc.xxxxx.xx:port/xxx     
       
    * rtc_username = your RTC user
    
            rtc_username = 'XXXXXX'
            
    * rtc_password = your RTC password
        
            rtc_password = 'XXXXX'
            
    * rtc_areas = Project areas from which you want to download the attachments, if you leave the field empty, 
                  you will get all the areas you have assigned in your RTC user.
                  to configure project areas it is necessary to do it in the following way:
                                    
             rtc_areas = 'Area1,Area2,Area3'
             IMPORTANT: do not leave spaces between values and the last value must be without a comma.
             
             if you want to download all the attachments from all the project areas, set it up like this:
             rtc_areas = ''                       
    * download_path = endpoint where you want to download the attachments
            
            windows example:  download_path = 'C:\\XXX\\XXX\\XXX\\RTC\\'
                              download_path = 'C:\\tmp\\RTC\\'
            
    * query_type = rtc types
                
             By default it looks for all rtc types:
             
             query_type = 'defect,tir,documentation_defect,fat_-_qualification_session,csip_entry,service_requests,' \
             'technical_documentation_review,release,procurement,change_request,legacy_or,' \
             'legacy_defects_cust-dev2,incident,Analysis_Level_4,problem,deliverable,meeting_action,task,' \
             'projectchangerequest,issue,com.ibm.team.workitem.workItemType.businessneed,' \
             'com.ibm.team.workitem.workItemType.risk,com.ibm.team.workitem.workItemType.riskaction,' \
             'com.ibm.team.workitem.workItemType.milestone,test_task'
            
    * query_year = for a more detailed search you can search for workitems by year
    
            query_year = '2016,2017,2018,2019,2020'
            IMPORTANT: do not leave spaces between values and the last value must be without a comma.
     
    * query_configItem = configuration item of workitem
    
            query_configItem = 'XXXX Platform'
            IMPORTANT: with this property we can only put one value
            
## Execution
    1. Install python 3.8
    2. Execute prepare_environment.bat
    3. Configure the properties
    5. Execute start_rtc_attachement_downloader.bat