## Start the app locally
- Start & build the app
    ```sh
    docker compose up --build
    ```
    
- Clean docker junk
    ```sh
    docker compose down -v
    ```

## Endpoints Documentation

### Fetch All Records

- **GET** `/objects/`
    - `skip` - optional parameter, number of records to skip (default=0)
    - `limit` - optional parameter, number of records to return (default=100)

    ```sh
    curl 'http://localhost:8000/objects/?skip=0&limit=10'
    ```

### Filter by One Criterion (Name)

- **GET** `/object/`
    - `name` - required parameter, part of the name to filter by
    - `skip` - optional parameter, number of records to skip (default=0)
    - `limit` - optional parameter, number of records to return (default=100)

    ```sh
    curl 'http://localhost:8000/object/?name=apple'
    ```

### Add New Records

- **POST** `/object/`
    - Adds a new food item record. Requires a JSON body with food item details.

    ```sh
    curl -X 'POST' \
      'http://localhost:8000/object/' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "descrip": "New Food Item",
      "energy_kcal": 100.0
    }'
    ```

### Modify Existing Records

- **PUT** `/object/{food_item_id}`
    - `food_item_id` - required parameter, ID of the food item to update
    - Updates an existing food item record. Requires a JSON body with food item details to update.

    ```sh
    curl -X 'PUT' \
      'http://localhost:8000/object/4f429043-6bb4-44f2-b5a5-a74beb17828e' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "descrip": "Updated Food Item",
      "energy_kcal": 150.0
    }'
    ```

### Advanced Processing (Statistics)

- **GET** `/stats/`
    - No parameters required
    - Returns aggregated nutritional statistics, including average, minimum, and maximum values for key nutrients across all food items. Additionally, it categorizes foods into high, medium, and low energy density based on their calories per gram.

    ```sh
    curl 'localhost:8000/stats/'
    ```

    ### Response Example

    ```json
    {
        "average_nutrients": {
            "energy_kcal": 200,
            "protein_g": 10,
            "fat_g": 5,
            "carb_g": 30
        },
        "min_nutrients": {
            "energy_kcal": 50,
            "protein_g": 0,
            "fat_g": 0,
            "carb_g": 5
        },
        "max_nutrients": {
            "energy_kcal": 500,
            "protein_g": 25,
            "fat_g": 30,
            "carb_g": 60
        },
        "energy_density_distribution": {
            "high": 150,
            "medium": 300,
            "low": 550
        }
    }
    ```

- **GET** `/healthy-foods/`
    - `skip` (optional): The number of records to skip before starting to collect the result set. Defaults to `0`.
    - `limit` (optional): The maximum number of records to return. Defaults to `10`.
    
    Retrieves a list of food items considered healthy based on a simple nutrient scoring system, which prioritizes foods high in protein and fiber but lower in calories and saturated fats. Results are sorted by their nutrient score in descending order, allowing the top healthiest foods to be listed first.

    ```sh
    curl 'http://localhost:8000/healthy-foods/?skip=0&limit=10'
    ```
    
    ### Response Example

    ```json
    [
        {
            "ndb_no": "A1",
            "descrip": "Spinach, raw",
            "energy_kcal": 23,
            "protein_g": 2.9,
            "fat_g": 0.4,
            "carb_g": 3.6,
            "fiber_g": 2.2,
            "saturated_fats_g": 0.063,
            ...
            "nutrient_score": 25.7
        },
        {
            "ndb_no": "B2",
            "descrip": "Chicken breast, grilled",
            "energy_kcal": 165,
            "protein_g": 31,
            "fat_g": 3.6,
            "carb_g": 0,
            "fiber_g": 0,
            "saturated_fats_g": 1,
            ...
            "nutrient_score": 28.5
        }
    ]
    ```