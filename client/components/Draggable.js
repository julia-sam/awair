import React from 'react';

function Draggable({ children, onDragStart, onDragEnd }) {
    const handleDragStart = (e) => {
        e.dataTransfer.setData('text/plain', ''); 
        e.target.classList.add('dragging');
        onDragStart();
    };

    const handleDragEnd = (e) => {
        e.target.classList.remove('dragging');
        onDragEnd();
    };

    return (
        <div
            draggable
            onDragStart={handleDragStart}
            onDragEnd={handleDragEnd}
        >
            {children}
        </div>
    );
}

export default Draggable;
