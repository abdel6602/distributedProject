# Imports
from google.cloud import storage

def upload_image_to_gcs(bucket_name, filename):
    """Uploads an image to a GCS bucket.

    Args:
        bucket_name: The name of the bucket to upload the image to.
        image_data: The image data as bytes.
          filename: The filename for the uploaded image.
    """
  
    with open(filename, "rb") as image_file:
        image_data = image_file.read()

    # Authenticate using Application Default Credentials (ADC)
    storage_client = storage.Client()

  # Reference the bucket and blob (object)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(filename)

  # Upload the image data
    blob.upload_from_string(image_data, content_type="image/jpeg")

    print(f"Image {filename} uploaded to bucket {bucket_name}")

# # Example usage (replace with your data)
# bucket_name = "your-bucket-name"
# image_data = b"your_image_data_here"  # Replace with actual image data in bytes
# filename = "user_uploaded_image.jpg"  # Example dynamic filename

# upload_image_to_gcs(bucket_name, image_data, filename)
