# Use this docker command to setup database

```shell
docker run -p 5432:5432 -e POSTGRES_PASSWORD=password -e POSTGRES_DB=db -e POSTGRES_USER=mmFoodAdmin postgres


```

# CollectionPoint:
    id (Primary Key)
    street (VARCHAR)
    city (VARCHAR)
    state (VARCHAR)
    postal_code (VARCHAR)

# Account:
    id (Primary Key, Inherits from User)
    username (VARCHAR)
    password (VARCHAR)
    userType(ENUM)
    first_name (VARCHAR)
    last_name (VARCHAR)
    contact_number (VARCHAR)
    email (VARCHAR)
    street (VARCHAR)
    city (VARCHAR)
    state (VARCHAR)
    postal_code (VARCHAR)




