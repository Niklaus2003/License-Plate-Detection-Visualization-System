import ast
import cv2
import numpy as np
import pandas as pd

def draw_border(img, top_left, bottom_left):
    thickness = 25
    line_length = 150
    line_height = 100
    x1, y1 = top_left
    x2, y2 = bottom_left
    cv2.line(img, (x1, y1), (x1, y1 + line_height), (0, 255, 0), thickness)
    cv2.line(img, (x1, y1), (x1 + line_length, y1), (0, 255, 0), thickness)
    cv2.line(img, (x1, y2), (x1, y2 - line_height), (0, 255, 0), thickness)
    cv2.line(img, (x1, y2), (x1 + line_length, y2), (0, 255, 0), thickness)
    cv2.line(img, (x2, y1), (x2, y1 + line_height), (0, 255, 0), thickness)
    cv2.line(img, (x2, y1), (x2 - line_length, y1), (0, 255, 0), thickness)
    cv2.line(img, (x2, y2), (x2, y2 - line_height), (0, 255, 0), thickness)
    cv2.line(img, (x2, y2), (x2 - line_length, y2), (0, 255, 0), thickness)
    return img

# Utility for bbox parsing (robust)
def parse_bbox_str(bstr):
    return tuple(map(float, str(bstr).replace('[','').replace(']','').split()))

results = pd.read_csv("./test_interpolated.csv")
cap = cv2.VideoCapture('sample2.mp4')
out = cv2.VideoWriter(
    'output.mp4',
    cv2.VideoWriter_fourcc(*'mp4v'),
    int(cap.get(cv2.CAP_PROP_FPS)),
    (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
)

license_plate = dict()
for car_id in np.unique(results['car_id']):
    score_max = np.amax(results[results['car_id'] == car_id]['license_plate_bbox_score'])
    license_plate[car_id] = dict()
    license_plate[car_id]['license_number'] = results[
        (results['car_id'] == car_id) &
        (results['license_plate_bbox_score'] == score_max)
    ]['license_number'].values[0]
    cap.set(cv2.CAP_PROP_POS_FRAMES, results[
        (results['car_id'] == car_id) &
        (results['license_plate_bbox_score'] == score_max)
    ]['frame_nmr'].values[0])
    ret, frame = cap.read()
    bbox = parse_bbox_str(results[
        (results['car_id'] == car_id) &
        (results['license_plate_bbox_score'] == score_max)
    ]['license_plate_bbox'].values[0])
    x1, y1, x2, y2 = map(int, bbox)
    license_crop = frame[y1:y2, x1:x2]
    preview_width = 300
    aspect_ratio = license_crop.shape[0] / license_crop.shape[1]
    preview_height = int(preview_width * aspect_ratio)
    try:
        license_crop = cv2.resize(license_crop, (preview_width, preview_height))
    except:
        license_crop = np.zeros((preview_height, preview_width, 3), dtype=np.uint8)
    license_plate[car_id]['crop'] = license_crop

frame_nmr = -1
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_nmr += 1
    df = results[results['frame_nmr'] == frame_nmr]
    for idx, row in df.iterrows():
        bbox = parse_bbox_str(row['car_bbox'])
        x1, y1, x2, y2 = map(int, bbox)
        frame = draw_border(frame, (x1, y1), (x2, y2))
        lp_bbox = parse_bbox_str(row['license_plate_bbox'])
        lpx1, lpy1, lpx2, lpy2 = map(int, lp_bbox)
        cv2.rectangle(frame, (lpx1, lpy1), (lpx2, lpy2), (0,0,255), 10)
        crop = license_plate[row['car_id']]['crop']
        h, w = crop.shape[:2]
        overlay_x = int(lpx1)
        overlay_y = max(0, int(lpy1) - h - 15)
        if overlay_x + w > frame.shape[1]:
            overlay_x = frame.shape[1] - w - 10
        if overlay_y < 0:
            overlay_y = 10

        
        text_canvas_height = 80  # much larger for visibility
        canvas_y = max(0, overlay_y - text_canvas_height - 10)
        if canvas_y < 0:
            canvas_y = overlay_y + h + 10
        frame[canvas_y:canvas_y + text_canvas_height, overlay_x:overlay_x + w] = (255,255,255)
        plate_text = license_plate[row['car_id']]['license_number']
        font_scale = 2.2     # larger text
        thickness = 4        # bolder text
        (tw, th), _ = cv2.getTextSize(plate_text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
        tx = overlay_x + (w - tw) // 2
        ty = canvas_y + (text_canvas_height + th) // 2
        if ty > frame.shape[0] - 10:
            ty = frame.shape[0] - 10
        cv2.putText(frame, plate_text, (tx, ty), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0,0,0), thickness)

        # Show preview crop just above license plate
        frame[overlay_y:overlay_y + h, overlay_x:overlay_x + w] = crop

    out.write(frame)

cap.release()
out.release()
print("Done. Output saved as output.mp4")
