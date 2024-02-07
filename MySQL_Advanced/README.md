# Pre-Work Information

## Use “container-on-demand” to run MySQL
* Ask for container Ubuntu 18.04 - Python 3.7
* Connect via SSH
* Or via the WebTerminal
* In the container, you should start MySQL before playing with it:

### 1.) Install Docker (if not already installed)
```
sudo apt update
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker
```

### 2.) Pull MySQL Docker Image
```
sudo docker pull mysql
```

### 3.) Run MySQL Container
```
sudo docker run -d --name=mysql-container -e MYSQL_ROOT_PASSWORD=your_password mysql

```
* Replace your_password with your desired MySQL root password.

### 4.) Connect to MySQL
```
sudo docker exec -it mysql-container mysql -uroot -p
```
* You'll be prompted to enter the password you set in step 4.
You now have MySQL running in a container and can connect to it either directly through the command line or via SSH/WebTerminal.

# Project Assignments

### 0. We are all unique! - [0-uniq_users.sql]

SQL script that creates a table `users` following these requirements:

* Attributes:
  * `id`, integer, never null, auto increment and primary key
  * `email`, string (255 characters), never null and unique
  * `name`, string (255 characters)
* If the table already exists, the script does not fail
* Script can be executed on any database

### 1. In and not out - [1-country_users.sql]

SQL script that creates a table `users` following these requirements:

* Attributes:
  * `id`, integer, never null, auto increment and primary key
  * `email`, string (255 characters), never null and unique
  * `name`, string (255 characters)
  * `country`, enumeration of countries: `US`, `CO` and `TN`, never null (= default will be the first element of the enumeration, here `US`)
* If the table already exists, script does not fail
* Script can be executed on any database

### 2. Best band ever! - [2-fans.sql]

SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans.

Requirements:

* Imports table dump: `metal_bands.sql.zip`
* Column names must be: `origin` and `nb_fans`
* Script can be executed on any database

### 3. Old school band - [3-glam_rock.sql]

SQL script that lists all bands with `Glam rock` as their main style, ranked by their longevity.

Requirements:

* Imports table dump: `metal_bands.sql.zip`
* Column names are `band_name` and `lifespan` (in years)
* Uses attributes `formed` and `split` for computing the `lifespan`
* Script can be executed on any database

### 4. Buy buy buy - [4-store.sql]

SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

Quantity in the table `items` can be negative.

### 5. Email validation to sent - [5-valid_email.sql]

SQL script that creates a trigger that resets the attribute `valid_email` only when the `email` has been changed.

### 6. Add bonus - [6-bonus.sql]

SQL script that creates a stored procedure `AddBonus` that adds a new correction for a student.

Requirements:

* Procedure `AddBonus` takes three inputs (in this order):
  * `user_id`, a `user.id` value (assumes `user_id` is linked to an existing `users`)
  * `project_name`, a new or already existing `projects` - if no `projects.name` is found, it is created
  * `score`, the score value for the correction

### 7. Average score - [7-average_score.sql]

SQL script that creates a stored procedure `ComputeAverageScoreForUser` that computes and stores the average score for a student.  Note: An average score can be a decimal.

Requirements:

* Procedure `ComputeAverageScoreForUser` takes 1 input:
  * `user_id`, a `users.id` value (assumes `user_id` is linked to an existing `users`)

### 8. Optimize simple search - [8-index_my_names.sql]

SQL script that creates an index `idx_name_first` on the table `names` and the first letter of `name`.

Requirements:

* Imports table dump: `names.sql.zip`
* Only the first letter of `name` is indexed

### 9. Optimize search and score - [9-index_name_score.sql]

SQL script that creates an index `idx_name_first_score` on the table `names` and the first letter of `name` and the `score`.

Requirements:

* Imports table dump: `names.sql.zip`
* Only the first letter of `name` AND `score` must be indexed

### 10. Safe divide - [10-div.sql]

SQL script that creates a function `SafeDiv` that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

Requirements:

* Creates a function
* The function `SafeDiv` takes 2 arguments:
  * `a`, INT
  * `b`, INT
* Returns `a / b` or 0 if `b == 0`

### 11. No table for a meeting - [11-need_meeting.sql]

SQL script that creates a view `need_meeting` that lists all students that have a score under 80 (strict) and no `last_meeting` or more than 1 month.

Requirements:

* The view `need_meeting` returns all students names when:
  * Their score is under (strict) 80
  * AND no `last_meeting` date OR more than a month