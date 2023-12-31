# Module3 Project Gamma

## Getting started

You have a project repository, now what? The next section
lists all of the deliverables that are due at the end of the
week. Below is some guidance for getting started on the
tasks for this week.

## Install Extensions

- Prettier: <https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode>
- Black Formatter: <https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter>

## Deliverables

- [x] Wire-frame diagrams
- [ ] API documentation
- [x] GitLab issue board is setup and in use

## Project layout

The layout of the project is just like all of the projects
you did with `docker-compose` in module #2. You will create
a directory in the root of the repository for each service
that you add to your project just like those previous
projects were setup.

### Directories

Several directories have been added to your project. The
directories `docs` and `journals` are places for you and
your team-mates to, respectively, put any documentation
about your project that you create and to put your
project-journal entries. See the _README.md_ file in each
directory for more info.

The other directories, `ghi` and `api`, are services, that
you can start building off of.

Inside of `ghi` is a minimal React app that has an "under
construction" page. It is setup similarly to all of the
other React projects that you have worked on.

Inside of `api` is a minimal FastAPI application.
"Where are all the files?" you might ask? Well, the
`main.py` file is the whole thing, and go take look inside
of it... There's not even much in there..., hmm? That is
FastAPI, we'll learn more about it in the coming days. Can
you figure out what this little web-application does even
though you haven't learned about FastAPI yet?

Also in `api` is a directory for your migrations.
If you choose to use PostgreSQL, then you'll want to use
migrations to control your database. Unlike Django, where
migrations were automatically created for you, you'll write
yours by hand using DDL. Don't worry about not knowing what
DDL means; we have you covered. There's a sample migration
in there that creates two tables so you can see what they
look like.

The Dockerfile and Dockerfile.dev run your migrations
for you automatically.

### Other files

The following project files have been created as a minimal
starting point. Please follow the guidance for each one for
a most successful project.

- `docker-compose.yaml`: there isn't much in here, just a
  **really** simple UI and FastAPI service. Add services
  (like a database) to this file as you did with previous
  projects in module #2.
- `.gitlab-ci.yml`: This is your "ci/cd" file where you will
  configure automated unit tests, code quality checks, and
  the building and deployment of your production system.
  Currently, all it does is deploy an "under construction"
  page to your production UI on GitLab and a sample backend
  to CapRover. We will learn much more about this file.
- `.gitignore`: This is a file that prevents unwanted files
  from getting added to your repository, files like
  `pyc` files, `__pycache__`, etc. We've set it up so that
  it has a good default configuration for Python projects.
- `.env.sample`: This file is a template to copy when
  creating environment variables for your team. Create a
  copy called `.env` and put your own passwords in here
  without fear of it being committed to git (see `.env`
  listed in `.gitignore`). You can also put team related
  environment variables in here, things like api and signing
  keys that shouldn't be committed; these should be
  duplicated in your deployed environments.

## How to complete the initial deploy

There will be further guidance on completing the initial
deployment, but it just consists of these steps:

### Setup GitLab repo/project

- make sure this project is in a group. If it isn't, stop
  now and move it to a GitLab group
- remove the fork relationship: In GitLab go to:

  Settings -> General -> Advanced -> Remove fork relationship

- add these GitLab CI/CD variables:
  - PUBLIC_URL : this is your gitlab pages URL
  - REACT_APP_API_HOST: enter "blank" for now

#### Your GitLab pages URL

You can't find this in GitLab until after you've done a deploy
but you can figure it out yourself from your GitLab project URL.

If this is your project URL

<https://gitlab.com/JDCT1/groove-genius>

then your GitLab pages URL will be

<https://JDCT1.gitlab.io/groove-genius>

### Initialize CapRover

1. Attain IP address and domain from an instructor
1. Follow the steps in the CD Cookbook in Learn.

### Update GitLab CI/CD variables

Copy the service URL for your CapRover service and then paste
that into the value for the REACT_APP_API_HOST CI/CD variable
in GitLab.

### Deploy it

Merge a change into main to kick off the initial deploy. Once the build pipeline
finishes you should be able to see an "under construction" page on your GitLab
pages site.

### API Endpoints

### User

#### Sign Up / Create user

- Endpoint path: /token
- Endpoint method: POST

- Request shape (form):

  - username: string
  - password: string
  - picture_url: string

- Response: Response will be the account info, status and a token.
- Response shape (JSON):

  ```json
  {
    "account": {
      "username": "Grandmaster Flash",
      "password": "password",
      "picture_url": "url"
    },
    "token": "token",
    "status": "status"
  }
  ```

#### Log In

- Endpoint path: /users/{id}
- Endpoint method: GET
- Query parameters:

  - username: Match username in database
  - password: Match password in database

- Headers:

  - Authentication: Bearer Token

- Request shape (form):

  - username: string
  - password: string

- Response: Response will be the account info and a token.
- Response shape (JSON):

  ```json
  {
    "account": {
      "username": "Grandmaster Flash",
      "password": "password",
      "picture_url": "url"
    },
    "token": "token"
  }
  ```

#### Log out

- Endpoint path: /token
- Endpoint method: DELETE

- Headers:

  - Authorization: Bearer token

- Response: True, since there's nothing to return.
- Response shape (JSON):

  ```json
  {
    "true": true
  }
  ```

### Edit User

- Endpoint path: /users/{id}
- Endpoint method: PUT

- Request shape:

```json
{
  "name": "Super Grandmaster Flash"
}
```

- Response: Response will be a status indicating whether it was successful or not.

### Playlist

#### Get Playlist List

- Endpoint path: /playlists
- Endpoint method: GET

- Response: Response will be the track info and status of request.
- Response shape (JSON):

```json
{
  "playlists": {
    {
      "id": id,
      "name": "Mixtape Supreme",
      "description": "Like a meal for your soul"
    },
    {
      "id": id,
      "name": "Playlist 2",
      "description": "Like a meal for your soul"
    },
  }
  },
  {
    "status": status
  }
```

#### Get Playlist by ID

- Endpoint path: /playlists/{id}
- Endpoint method: GET

- Response: Response will be the track info and status of request.
- Response shape (JSON):

```json
{
  "name": "Mixtape Supreme",
  "description": "Like a meal for your soul.",
  "id": id
  },
  {
    "status": status
  }
```


#### Create Playlist

- Endpoint path: /playlists
- Endpoint method: POST

- Request shape:

```json
{
  "user_id": user_id,
  "name": "Mixtape Supreme",
  "description": "Like a meal for your soul."
}
```

- Response: Response will be status and playlist info.
- Response shape (JSON):

  ```json
  {
    "playlist": {
      "user_id": user_id,
      "name": "Mixtape Supreme",
      "description": "Like a meal for your soul.",
    },
    "status": status
  }
  ```

#### Edit Playlist

- Endpoint path: /playlists/{id}
- Endpoint method: PUT

- Request shape:

```json
{
  "name": "Super Mixtape Supreme"
}
```

- Response: Response will be a status indicating whether it was successful or not.

#### Delete Playlist

- Endpoint path: /playlists/{id}
- Endpoint method: DELETE

- Response will be the status, since there's nothing to return.
- Response shape:

```json
{
  "true": true
}
```

### Track

#### Get Track List

- Endpoint path: /tracks
- Endpoint method: GET

- Request shape:

```json

{
  "title": "Jump",
  "artist": "Van Halen",
  "genre_id": genre_id,
  "album": "1984"
}
```

- Response: Response will be the track info and status of request.
- Response shape (JSON):

```json
{
  "title": "Jump",
  "artist": "Van Halen",
  "genre_id": genre_id,
  "album": "1984"
  },
  {
    "status": status
  }
```

#### Get Track by ID

- Endpoint path: /tracks/{id}
- Endpoint method: GET

- Request shape:

```json
{
  "title": "Jump",
  "artist": "Van Halen",
  "genre_id": genre_id,
  "album": "1984"
}
```

- Response: Response will be the track info and status of request.
- Response shape (JSON):

```json
{
  "title": "Jump",
  "artist": "Van Halen",
  "genre_id": genre_id,
  "album": "1984",
  "id": id
  },
  {
    "status": status
  }
```

#### Create Track

- Endpoint path: /tracks
- Endpoint method: POST

- Request shape:

```json
{
  "title": "Jump",
  "artist": "Van Halen",
  "genre_id": genre_id,
  "album": "1984"
}
```

- Response: Response will be the track info and status of request.
- Response shape (JSON):

```json
{
  "track": {
    "title": "Jump",
    "artist": "Van Halen",
    "genre_name": "Rock/Pop",
    "album": "1984"
  },
  {
    "status": status
  }
}
```

#### Edit Track

- Endpoint path: /tracks/{id}
- Endpoint method: PUT

- Request shape:

```json
{
  "title": "Jump!"
}
```

- Response: Response will be new info and success/failure status.
- Response shape(JSON):

```json
{
  "track": {
  "title": "Jump!"
  },
  {
    "status": status
  }
}
```

#### Delete Track

- Endpoint path: /tracks/{id}
- Endpoint method: DELETE

- Response will be the status, since there's nothing to return.
- Response shape:

```json
{
  "true": true
}
```

### Genre

#### Get Genre List

- Endpoint path: /genres
- Endpoint method: GET

- Request shape:

```json
{
  "name": "Rock/Pop"
}
```

- Response: Response will be the track info and status of request.
- Response shape (JSON):

```json
{
  "name": "Rock/Pop"
  },
  {
    "status": status
  }
```

#### Get Genre by ID

- Endpoint path: /genres/{id}
- Endpoint method: GET

- Request shape:

```json
{
  "name": "Rock/Pop"
}
```

- Response: Response will be the track info and status of request.
- Response shape (JSON):

```json
{
  "name": "Rock/Pop",
  "id": id
  },
  {
    "status": status
  }
```

#### Create Genre

- Endpoint path: /genres
- Endpoint method: POST

- Request shape:

```json
{
  "id": 1,
  "name": "Rock/Pop",
}
```

- Response: Response will be the track info and status of request.
- Response shape (JSON):

```json
{
  "name": "Rock/Pop"
  },
  {
    "status": status
  }
```

#### Edit Genre

- Endpoint path: /genres/{id}
- Endpoint method: PUT

- Request shape:

```json
{
  "name": "Rock/Pop"
}
```

- Response: Response will be new info and success/failure status.
- Response shape(JSON):

```json
{
  "name": "Rock/Pop"
  },
  {
    "status": status
  }
```

#### Delete Genre

- Endpoint path: /genres/{id}
- Endpoint method: DELETE

- Response will be the status, since there's nothing to return.
- Response shape:

```json
{
  "true": true
}
```

### Recommendations

#### Get Previous Recommendations

- Endpoint path: /recommendations
- Endpoint method: GET

- Response will be the id, genres, track id
- Response shape:

```json
{
  "recommendations": {
    "id": id,
    "genre": "genre",
    "track_id": track_id
    },
    {
    "id": id,
    "genre": "genre",
    "track_id": track_id
    },
}
```

#### Get Recommendation

- Endpoint path: /recommendations/{id}
- Endpoint method: GET

- Response will be the id, genres, track id
- Response shape:

```json
{
  "id": id,
  "genre": "genre",
  "track_id": track_id
}
```

#### Delete Recommendation

- Endpoint path: /recommendations/{id}
- Endpoint method: DELETE

- Response will be the status, since there's nothing to return.
- Response shape:

```json
{
  "true": true
}
```
