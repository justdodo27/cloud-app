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
