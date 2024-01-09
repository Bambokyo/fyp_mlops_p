# fyp_mlops_p

### Pose Quest: Efficient pose retrieval from large motion Databases
Human Pose Estimation (HPE) in computer vision has gained prominence in applications like animation, gaming, and virtual reality. The challenge arises from managing high-dimensional data and non-Euclidean metrics in vast motion databases. This paper addresses the problem of compromised efficiency and speed in existing pose retrieval systems due to the exponential growth of visual data. The research problem lies in the need for innovative solutions to ensure precise and timely access to pose data in a complex data landscape. We aim to develop enhanced, adaptive methodologies for efficient and accurate pose retrieval, bridging the gap between abundant yet intricate visual data and the requirements of professionals and industries relying on HPE. This work redefines the HPE landscape by offering agile solutions to navigate this evolving challenge.

![alt text](https://github.com/Bambokyo/fyp_mlops_p/blob/main/PoseMethodology.png?raw=true)

### Methodology
Cosine similarity computes the cosine of the angle between two vectors, in this case, the pose vectors from our dataset. This measure ranges from -1 indicating exactly opposite, to 1 indicating exactly the same, with 0 typically denoting independence. Our implementation in Python capitalized on vectorized operations for rapid computation.
### Experimentation and Parameters
Our experimentation was straightforward: we computed the cosine similarity for each pair of poses between our query dataset and the extensive motion database. No parameter tuning was required for this method, making it an attractive option for scenarios where simplicity and speed are paramount.
### Evaluation Metrics
The retrieval effectiveness was gauged by the cosine similarity scores, where a score of 1.0000 represented a perfect match. The retrieval time was also recorded, providing insights into the method's efficiency.

