import json
import yaml

def serialize_deserialize(data, type='j', mode='s'):
    try:
        if type.lower() == 'j':
            if mode.lower() == 's':
                return json.dumps(data)

            elif mode.lower() == 'd':
                return json.loads(data)

            else:
                raise ValueError("Mode must be 's' for Serialize or 'd' for Deserialize.")

        elif type.lower() == 'y':
            if mode.lower() == 's':
                return yaml.dump(data)

            elif mode.lower() == 'd':
                return yaml.safe_load(data)

            else:
                raise ValueError("Mode must be 's' for Serialize or 'd' for Deserialize.")

        else:
            raise ValueError("Unsupported type. Use 'j' for JSON or 'y' for YAML.")

    except Exception as error:
        print (f"Error during {mode} operation: {error}")
        return None

def main():
    print("Serialization and Deserialization of JSON/YAML file")
    print("Choose File Type - JSON (j) or YAML (y), \and Mode - Serialize (s) or Deserialize (d): ")
    user = input("=> ").strip().lower()

    file, mode = user.split(',')

    file_path = input("Give path to the file")

    serialize_deserialize(file_path, file, mode)

   
if __name__ == "__main__":
   main()
