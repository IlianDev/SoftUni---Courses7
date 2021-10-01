function createRect(width, height) {
    const rect = {
        width: width,
        height: height,    
    };
    rect.getArea = () => {
        return rect.width * rect.height;
    }
    return rect;
}

const rectangle = createRect(100, 200);
console.log(rectangle.getArea());
