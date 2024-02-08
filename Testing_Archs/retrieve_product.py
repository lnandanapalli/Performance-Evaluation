import requests
import threading
import time
import matplotlib.pyplot as plt

product_details_url = "http://18.212.112.226/details/65700c8f5ce2e548892542e8"
concurrent_users = 100
total_requests = 1000
response_times = []
success_count = 0
error_count = 0

def send_requests(url, num_requests):
    global success_count
    global error_count
    for _ in range(num_requests):
        start_time = time.time()
        try:
            response = requests.get(url)
            
            if response.status_code == 200:
                success_count += 1
            else:
                error_count += 1
        except Exception as e:
            print(f"Error accessing {url}: {e}")
            error_count += 1
        finally:
            end_time = time.time()
            response_times.append(end_time - start_time)

def run_load_test(url, concurrent_users, total_requests):
    
    requests_per_user = total_requests // concurrent_users
    
    threads = []
    for _ in range(concurrent_users):
        thread = threading.Thread(target=send_requests, args=(url, requests_per_user))
        threads.append(thread)
    
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()
        
if __name__ == "__main__":
    print("Starting load test for the product details URL...")
    run_load_test(product_details_url, concurrent_users, total_requests)
    print("Load test for the product details URL completed.")
    
    average_response_time = sum(response_times) / len(response_times)
    success_rate = success_count / total_requests
    error_rate = error_count / total_requests
    print("\nMetrics for the product details URL:")
    print(f"Average Response Time: {average_response_time:.4f} seconds")
    print(f"Success Rate: {success_rate * 100:.2f}%")
    print(f"Error Rate: {error_rate * 100:.2f}%")
    
    plt.figure(figsize=(10, 6))
    plt.hist(response_times, bins=20, color='orange', alpha=0.7)
    plt.title('Response Time Distribution - Product Details URL')
    plt.xlabel('Response Time (seconds)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
