SELECT W2.Id 
FROM Weather AS W1, Weather AS W2
WHERE DATEDIFF(W2.RecordDate, W1.RecordDate) = 1
AND W1.Temperature < W2.Temperature