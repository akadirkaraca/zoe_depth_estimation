
# Zoe Depth Estimation Project




## Usage/Examples

### CLI Usage
```bash
usage: cli.py [-h] input_image output_image    

Depth Estimation using ZoeDepth.

positional arguments:
  input_image   Path the input image.
  output_image  Path the output depth map.     

optional arguments:
  -h, --help    show this help message and exit
```

### API Usage

http://127.0.0.1:8041/predict

## Installation

Install depth estimation project with pip

```bash
pip install -r requirenments.txt
```
    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`IMAGE_API_KEY`



## Deployment

To deploy this project run

```bash
  docker build -t depth_estimation .
  docker run -d -t 8041:8041 depth_estimation
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

