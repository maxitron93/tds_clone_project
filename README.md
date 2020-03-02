A clone of [towardsdatascience.com](https://towardsdatascience.com/)

# Planning

## Functionality (backend-related)

### Stories App

Users can read stories.

API requirements

- get story by title (with associated sections, tags, claps, and author) 
- get the number of responses to the story
- allow reader to follow the author
- allow user to clap for story

![Story](readme_assets/story.PNG)

Users can view responses for each story, and write or edit their response.

API requirements
- get responses by story (with associated claps, user)
- allow user to create a response
- allow user to edit their response
- allow user to delete their response

![Response](readme_assets/response.PNG)

Users can write new stories and publish them. Stories can include titels, text, images, quotes, gifs







Users can saves stories as draft, edit published stories




Users can set and change SEO title and description. Users can also add and remove tags, and delete the whole story.





Admin can...
- add admin tags to stories
- remove admin tags to stories

<strong>Profiles App</strong>

Users can...
- create an account
- log in
- log out
- update account details
- update profile details
- delete account

Users can...
- clap for stories 
- follow other users
- unfollow other users
- save story as 'saved'
- save story as 'archived'

Users can...
- view list of 'saved' stories
- view lsit of 'archived stories'
- view list of 'recently viewed' stories
- view list of clapped stories
- view list of who they're following
- view list of who's following them

<strong>Topics App</strong>

Admin can...
- create topics
- edit topics
- delete topic

Admin can...
- add subtopics to topics (by tags)
- add subtopics to topics (via admin tags)
- edit subtopics
- remove subtopics from topics

Users can...
- view topics and subtopics
- view stories of users they're following
- view stories under a subtopic
- search for stories by tag


## Database Architecture
<strong>Stories App</strong>

![Stories App](readme_assets/stories_app.PNG)

<strong>Profiles App</strong>

![Profiles App](readme_assets/profiles_app.PNG)

<strong>Topics App</strong>

![Topics App](readme_assets/topics_app.PNG)

