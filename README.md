# YOUTUBE VIDEOS SNIPPER

## Description
• An API to fetch latest videos sorted in reverse order of their publishing date-time from YouTube.</br>
• Using Celery for task queue with Redis as a message broaker.</br>
• Search api supports case-insensitive partial matches.</br>

## Public Api's
• List View => http://localhost:8000/</br>
• Detail View => http://localhost:8000/{id}</br>
• Wild Searching either on description or title => http://localhost:8000/?search={text}</br>
• Sorted results either on published_on or created_at => http://localhost:8000/?ordering=published_on</br>
• Paginated Responses with ?page={number} for all the requests</br>  

## Set Up Procedure
### Clone This Repo And Execute

```bash
$git clone https://github.com/9643kavinder/YT-Videos-Snipper.git
cd YT-Videos-Snipper
docker-compose up
```

## Screenshots
<p align="center">
  <img src="https://github.com/9643kavinder/YT-Videos-Snipper/blob/main/screenshots/2.png" />
 </p>
 <p align="center">
  <img src="https://github.com/9643kavinder/YT-Videos-Snipper/blob/main/screenshots/1.png"/>
 </p>
