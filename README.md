# Satellite Image Enhancement using Point Processing Techniques

## 📌 Introduction
Satellite imagery often suffers from atmospheric interference, low contrast, and poor visibility of surface features, making it challenging for environmental monitoring, urban planning, and agricultural analysis. Enhancing these images can reveal hidden terrain details, improve vegetation contrast, and support more accurate land-use classification.

This project focuses on improving the visibility of surface features and terrain details in low-contrast satellite images using logarithmic transformation and histogram equalization techniques.

## 📂 Dataset
**Source:** [kaggle-satellite-image-caption-generation Dataset](https://www.kaggle.com/datasets/tomtillo/satellite-image-caption-generation)

- Contains multispectral satellite images in various formats (TIFF, JPEG)
- Resolution: 30m per pixel for visible bands
- Coverage: Various geographical regions including urban, agricultural, and natural landscapes
- Challenges: Images affected by atmospheric haze, shadow regions, and varying illumination conditions
- Quality control: Images selected for clear weather conditions but with typical contrast limitations

## ⚙️ Prerequisites
Before running the project, install the following dependencies:

```bash
pip install opencv-python matplotlib numpy 
```

For satellite image processing, additional libraries may be helpful:
```bash
pip install rasterio pillow
```

## 🔬 Methodology & Justification

### 1. Logarithmic Transformation
**Justification:** Enhances visibility in darker shadow regions while compressing bright areas. Particularly useful for revealing details in shadowed valleys and urban areas.

**Function:**
$$s = c \times \log(1 + r)$$

where c is a scaling constant and r is the input pixel intensity.

### 2. Histogram Equalization
**Justification:** Redistributes pixel intensities across the full dynamic range, improving global contrast between different land cover types (water, vegetation, urban areas).

**Function:** Maps the cumulative distribution function to achieve uniform histogram distribution across 0-255 intensity range.

### 3. Logarithmic + Histogram Equalization (Combination)
**Justification:** Logarithmic transformation first enhances shadow details and terrain features, while histogram equalization redistributes contrast globally. This combination provides optimal visibility for both dark terrain features and overall landscape contrast.

## 📊 Results & Analysis

**Logarithmic Transformation:** Significantly improved visibility in shadow regions and dark terrain features, but limited improvement in overall contrast.

**Histogram Equalization:** Strong global contrast enhancement, clearly distinguishing between water bodies, vegetation, and urban areas, but sometimes over-enhanced bright regions.

**Combination (Logarithmic + Histogram Equalization):** Provided the most comprehensive enhancement, balancing shadow detail visibility with global contrast optimization.

### Histogram Behavior Summary (Quick Guide)
- **Logarithmic Transform:** Histogram shifts toward higher intensities, expanding dark region details
- **Histogram Equalization:** Histogram flattens and spreads across full 0-255 range
- **Combination:** Histogram shows both expanded dark regions and uniform distribution for balanced enhancement

## 🎯 Applications
- **Environmental Monitoring:** Enhanced vegetation and water body detection
- **Urban Planning:** Improved visibility of infrastructure and development patterns  
- **Agricultural Analysis:** Better crop health assessment and field boundary identification
- **Geological Surveys:** Enhanced terrain feature recognition and topographic analysis

## 📈 Conclusion
The combination of **Logarithmic Transformation + Histogram Equalization** provided the most effective results for satellite image enhancement.

This combination successfully enhanced subtle terrain details while redistributing global contrast for optimal feature discrimination.

**Recommendation:** For satellite image enhancement tasks, particularly for multi-purpose analysis, apply Logarithmic → Histogram Equalization for optimal clarity and feature visibility.

## 💻 Usage
```bash
python assignment.py airport_5.jpg
```

The script will:
1. Load the input satellite image
2. Apply logarithmic transformation and histogram equalization
3. Display original vs enhanced image comparison with histograms

## 📂 Code

The fully-commented code is available :

- Check the attached `.py` file in this repository.

## 👨‍💻 Author
**Name:** Mehar Akbar  
**Contact:** [Mehar Akbar]meher2ch@gmail.com 
