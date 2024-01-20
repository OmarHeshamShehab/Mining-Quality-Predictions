import sys
import seaborn as sns
import tensorflow as tf

print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)
print(f"Seaborn version: {sns.__version__}")

tf.config.list_physical_devices("GPU")
tf.test.is_gpu_available()

import tensorflow as tf
if tf.config.list_physical_devices('GPU'):
    print('GPU Supported')
else:
    print('GPU Not Supported')
