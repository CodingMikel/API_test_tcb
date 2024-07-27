from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

# In-memory data store for pools
pools = {}

@app.route('/append', methods=['POST'])
def append_to_pool():
    data = request.get_json()
    pool_id = data['poolId']
    pool_values = data['poolValues']
    
    if pool_id in pools:
        pools[pool_id].extend(pool_values)
        status = "appended"
    else:
        pools[pool_id] = pool_values
        status = "inserted"
    print(pools)
    return jsonify({"status": status})

@app.route('/query', methods=['POST'])
def query_pool():
    data = request.get_json()
    pool_id = data['poolId']
    percentile = data['percentile']
    
    if pool_id not in pools:
        return jsonify({"error": "Pool not found"}), 404
    
    pool_values = pools[pool_id]
    total_count = len(pool_values)
    
    if total_count < 100:
        quantile_value = calculate_quantile(pool_values, percentile)
    else:
        quantile_value = np.percentile(pool_values, percentile)
    
    return jsonify({"quantile": quantile_value, "totalCount": total_count})

def calculate_quantile(values, percentile):
    """Calculate the quantile manually if less than 100 values."""
    sorted_values = sorted(values)
    position = (len(sorted_values) - 1) * percentile / 100
    floor = int(position)
    fractional = position - floor
    if floor + 1 < len(sorted_values):
        return sorted_values[floor] + (sorted_values[floor + 1] - sorted_values[floor]) * fractional
    else:
        return sorted_values[floor]

if __name__ == '__main__':
    app.run(debug=True)
