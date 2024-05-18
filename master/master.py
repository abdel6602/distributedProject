import pika
import base64

# RabbitMQ connection details (replace with your own)


def main(filename, operation, params, id):
  connection_parameters = pika.ConnectionParameters(host='104.199.5.58')
  connection = pika.BlockingConnection(connection_parameters)
  channel = connection.channel()

  # Declare the queue for image processing tasks
  channel.queue_declare(queue='image_processing_tasks', durable=False)

  params = params.split(',')
  
  def process_image_request(image_path):
    # Read image data
    with open(filename, 'rb') as f:
      image_data = f.read()
    # Create task message
    task_message = base64.b64encode(image_data) + f'\n{operation}'.encode()
    for param in params:
      task_message += f'\n{param}'.encode()
    # append id to message
    task_message += f'\n\n{id}'.encode()

    # Publish task message to the queue
    channel.basic_publish(exchange='',
                          routing_key='image_processing_tasks',
                          body=task_message)
    print(f"Sent image processing task for {image_path}")
  
  process_image_request(filename)
    
  connection.close()
  return True, id

  # Listen for image paths to process (replace with your logic to receive requests)
  # while True:
  #   image_path = input("Enter image path to process (or 'q' to quit): ")
  #   if image_path.lower() == 'q':
  #     break
  #   operation = input("Enter operation to perform: ").lower()
  #   process_image_request(image_path)


if __name__ == '__main__':
  import json  # Import for JSON serialization (assuming you use it)
  main()
