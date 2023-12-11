from sklearn.neighbors import NearestNeighbors, BallTree
import numpy as np
import time
import mlflow

# Set the tracking URI to a local directory
# mlflow.set_tracking_uri("D:\\University\\FYP\\Implementation\\HDM_01-01_amc\\mlflow")  # Replace "/path/to/mlflow" with your desired directory

def knn_M(query, dataset, K, method='knn', metric='euclidean'):
    with mlflow.start_run():
        mlflow.log_param("K", K)
        mlflow.log_param("method", method)
        mlflow.log_param("metric", metric)

        if method == 'knn':
            knn = NearestNeighbors(n_neighbors=K, algorithm='auto', metric=metric)
            knn.fit(dataset)
        elif method == 'range':
            knn = BallTree(dataset, metric=metric)

        # Perform K-nearest neighbor search or range search for the query matrix
        start_time = time.time()
        if method == 'knn':
            distances, indices = knn.kneighbors(query)
        elif method == 'range':
            indices = knn.query_radius(query, r=55.0)
        retrieval_time = time.time() - start_time

        # Initialize variables to store evaluation metrics
        mpjse_list = []
        pck_list = []

        # Calculate evaluation metrics for each query pose
        for i in range(len(query)):
            if method == 'knn':
                nearest_neighbors = dataset[indices[i]]
            elif method == 'range':
                nearest_neighbors = dataset[indices[i]]

            mpjse = np.mean(np.linalg.norm(query[i] - nearest_neighbors, axis=1))
            mpjse_list.append(mpjse)

            threshold = 30
            A = np.linalg.norm(query[i] - nearest_neighbors, axis=1)
            correct_keypoints = A < threshold
            pck = np.sum(correct_keypoints) / len(correct_keypoints)
            pck_list.append(pck)

        mean_mpjse = np.mean(mpjse_list)
        mean_pck = np.mean(pck_list)

        mlflow.log_metric("mean_mpjse", mean_mpjse)
        mlflow.log_metric("mean_pck", mean_pck)
        mlflow.log_metric("retrieval_time", retrieval_time)

        # Save the model as an artifact
        mlflow.sklearn.log_model(sk_model=knn, artifact_path="knn_model")

        print(f"Method: {method}")
        print(f"Metric: {metric}")
        print(f"Mean Per Joint Squared Error (MPJSE): {mean_mpjse}")
        print(f"Percentage of Correct Keypoints (PCK): {mean_pck}")
        print(f"Retrieval Time: {retrieval_time} seconds")

        return mean_pck

# Example usage
query = np.random.rand(10, 3)  # Replace this with your actual query
dataset = np.random.rand(100, 3)  # Replace this with your actual dataset
k_value = 32

knn_M(query, dataset, K=k_value, method='knn', metric='euclidean')
