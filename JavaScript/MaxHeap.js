class MaxHeap {
    constructor() {
        this.heap = [0];
        this.length = 0;
    }

    add(num) {
        this.heap.push(num);
        ++this.length;

        this.moveUp(this.length - 1);
    }

    moveUp(position) {
        let parentPosition = Math.floor(position / 2);

        while (parentPosition > 0) {
            if (this.heap[position] > this.heap[parentPosition]) {
                [this.heap[position], this.heap[parentPosition]] = [this.heap[parentPosition], this.heap[position]];
            }

            position = parentPosition;
            parentPosition = Math.floor(position / 2);
        }
    }

    extract() {
        let num = this.heap[1];
        this.heap[1] = this.heap[this.length];
        --this.length;

        this.moveDown(1);
        this.heap.pop();
        return num;
    };

    moveDown(position) {

        while (position * 2 <= this.length) {
            let maxChildPos = this.findMaxChildPos(position);

            if (this.heap[position] < this.heap[maxChildPos]) {
                [this.heap[position], this.heap[maxChildPos]] = [this.heap[maxChildPos], this.heap[position]]
            };

            position = maxChildPos
        }
    }

    findMaxChildPos(position) {
        let leftChildPos = position * 2;
        let rightChildPos = (position * 2) + 1;

        if (rightChildPos > this.length) return leftChildPos;
        else if (this.heap[rightChildPos] > this.heap[leftChildPos]) return rightChildPos;
        else return leftChildPos;
    }

    createHeap(numArray) {
        let len = numArray.length;
        this.heap = [0, ...numArray];
        this.length = len;

        let position = Math.floor(len / 2);

        while (position > 0) {
            this.moveDown(position);
            --position;
        }


    }
}