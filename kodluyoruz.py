import math

points = [(0, 0), (3, 4), (5, 1)] 

# Öklid Mesafesi Fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Mesafelerin Hesaplanması
distances = [] 
for i in range(len(points)):
    for j in range(i + 1, len(points)):  
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)  


min_distance = min(distances)  
print(f"Noktalar arasındaki minimum Öklid mesafesi: {min_distance}")
