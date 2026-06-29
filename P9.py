import cv2
import numpy as np
def estimate_alpha(image, trimap):
    # Placeholder function, replace with your matting algorithm implementation
    # This example simply sets alpha values based on trimap (e.g., foreground = 1, background = 0, unknown = interpolated)
    alpha = np.zeros_like(trimap, dtype=np.float32)
    alpha[trimap == 255] = 1.0  # Foreground
    alpha[trimap == 0] = 0.0  # Background
    alpha[(trimap > 0) & (trimap < 255)] = 0.5  # Interpolated
    return alpha

def image_matting(image, trimap):
    # Convert image and trimap to float32
    image = image.astype(np.float32) / 255.0
    trimap = trimap.astype(np.float32) / 255.0

    # Estimate alpha matte using a matting algorithm
    # Replace this with your desired matting algorithm
    alpha = estimate_alpha(image, trimap)

    # Clip alpha values to [0, 1]
    alpha = np.clip(alpha, 0, 1)

    return alpha

def composit_foreground_background(foreground, background, alpha):
    # Resize background to match the foreground size
    background = cv2.resize(background, (foreground.shape[1], foreground.shape[0]))

    # Convert alpha to 3 channels
    alpha = np.stack((alpha, alpha, alpha), axis=2)

    # Composite foreground and background using alpha matte
    composited_image = alpha * foreground + (1 - alpha) * background

    return composited_image

# Example usage
if __name__ == "__main__":
    # Read foreground, background, and trimap images
    foreground = cv2.imread("C:/Users/Darshana/OneDrive/Desktop/MSCIT SEM 2/MSC IT SEM 2 COMPUTER VISION/model.jpg")
    background = cv2.imread("C:/Users/Darshana/OneDrive/Desktop/MSCIT SEM 2/MSC IT SEM 2 COMPUTER VISION/model.jpg")
    trimap = cv2.imread("C:/Users/Darshana/OneDrive/Desktop/MSCIT SEM 2/MSC IT SEM 2 COMPUTER VISION/model.jpg", cv2.IMREAD_GRAYSCALE)

    # Perform image matting
    alpha = image_matting(foreground, trimap)

    # Perform compositing
    composited_image = composit_foreground_background(foreground, background, alpha)

    # Display result
    cv2.imshow("Composited Image", composited_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
