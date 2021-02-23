import argparse
import imutils
import cv2


def main():
	image = "images/image.png"

	# Using opencv to apply grayscale, gaussian blur and threshold
	img = cv2.imread(image)
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img_blur = cv2.blur(img_gray, (3, 3))
	img_canny = cv2.Canny(img_blur, 40, 95)

	cv2.imshow("gray", img_gray)
	cv2.imshow("blur", img_blur)
	cv2.imshow("canny", img_canny)
	# Find contours
	cnts = cv2.findContours(img_canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)

	for c in cnts:

		# Convex Hull
		epsilon = 0.02 * cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, epsilon, True)

		# Draw contour
		cv2.drawContours(img, [approx], -1, (0, 255, 0), 1)

		shape_text = ""

		if len(approx) == 3:
			shape_text = "Triangle"
		elif len(approx) == 4:
			shape_text = "Rectangle"
		elif len(approx) == 5:
			shape_text = "Pentagon"
		elif len(approx) == 6:
			shape_text = "Hexagon"
		else:
			shape_text = "Circle"

		cv2.putText(img, shape_text, (approx[0][0][0] - 10, approx[0][0][1] - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)

	cv2.imshow("Image", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == "__main__":
	main()