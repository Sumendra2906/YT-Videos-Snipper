#YOUTUBE VIDEOS SNIPPER
#Description

• An API to fetch latest videos sorted in reverse order of their publishing date-time from YouTube.
• Using Celery for task queue with Redis as a message broaker.
• Search api supports case-insensitive partial matches.
#Public Api's

• List View => http://localhost:8000/
• Detail View => http://localhost:8000/{id}
• Wild Searching either on description or title => http://localhost:8000/?search={text}
• Sorted results either on published_on or created_at => http://localhost:8000/?ordering=published_on
• Paginated Responses with ?page={number} for all the requests
#Set Up Procedure
#Clone This Repo And Execute

$git clone https://github.com/9643kavinder/YT-Videos-Snipper.git
cd YT-Videos-Snipper
docker-compose up

#Screenshots


