import requests
import threading
import time
import matplotlib.pyplot as plt

monolithic_url = "http://54.208.228.118/"
microservices_url = "http://18.212.112.226/"
concurrent_users = 1000
total_requests = 10000
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
    print("Starting load test for the monolithic app...")
    run_load_test(monolithic_url, concurrent_users, total_requests)
    print("Load test for the monolithic app completed.")
    
    average_response_time = sum(response_times) / len(response_times)
    success_rate = success_count / total_requests
    error_rate = error_count / total_requests
    print("\nMetrics for the monolithic app:")
    print(f"Average Response Time: {average_response_time:.4f} seconds")
    print(f"Success Rate: {success_rate * 100:.2f}%")
    print(f"Error Rate: {error_rate * 100:.2f}%")
    
    plt.figure(figsize=(10, 6))
    plt.hist(response_times, bins=20, color='blue', alpha=0.7)
    plt.title('Response Time Distribution - Monolithic App')
    plt.xlabel('Response Time (seconds)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
    print("\nStarting load test for the microservices app...")
    
    response_times = []
    success_count = 0
    error_count = 0
    run_load_test(microservices_url, concurrent_users, total_requests)
    print("Load test for the microservices app completed.")
    
    average_response_time = sum(response_times) / len(response_times)
    success_rate = success_count / total_requests
    error_rate = error_count / total_requests
    print("\nMetrics for the microservices app:")
    print(f"Average Response Time: {average_response_time:.4f} seconds")
    print(f"Success Rate: {success_rate * 100:.2f}%")
    print(f"Error Rate: {error_rate * 100:.2f}%")
    
    plt.figure(figsize=(10, 6))
    plt.hist(response_times, bins=20, color='green', alpha=0.7)
    plt.title('Response Time Distribution - Microservices App')
    plt.xlabel('Response Time (seconds)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
