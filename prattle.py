# Tutorial example. Doesn't depend on any third party GUI framework.
# Tested with CEF Python v57.0+

from cefpython3 import cefpython as cef
import base64
import platform
import sys
import threading
import ctypes
import platform
import csv
from io import StringIO
import json
import pandas
import numbers
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import base64
import io 

# HTML code. Browser will navigate to a Data uri created
# from this html code.
HTML_code = """
<!doctype html>
<html>

<head>
    <meta charset="utf-8">

    <style text="text/css">

.modal {
    display: none; /* Hidden by default */
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    padding-top: 60px; /* Location of the box */
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}

/* Modal Content */
.modal-content {
    position: relative;
    background-color: #fefefe;
    margin: auto;
    padding: 0;
    top: 150px;
    border: 1px solid #888;
    width: 70%;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2),0 6px 20px 0 rgba(0,0,0,0.19);
    -webkit-animation-name: fadeIn;
    -webkit-animation-duration: 0.4s;
    animation-name: fadeIn;
    animation-duration: 0.4s
}

.modal-header {
    padding: 2px 16px;
    background-color: #5cb85c;
    color: white;
}

.modal-body {padding: 16px 20px; display:block;}

.modal-btn {
     position: relative;
     border: none; /* Remove borders */
     color: white;
     background-color: #4CAF50; /* Add a backgriund color */
     padding: 12px 20px;
     margin: 4px 2px;
     border-radius: 4px;
     left: -15px;
     cursor: pointer; /* Add a pointer cursor on mouse-over */
}

.modal-btn:hover {
    opacity: 0.8;
}

.modal-small-btn {
    position: relative;
    border: none; /* Remove borders */
    color: white;
    background-color: #4CAF50; /* Add a backgriund color */
    padding: 4px 4px;
    margin: 2px 2px;
    border-radius: 4px;
    cursor: pointer; /* Add a pointer cursor on mouse-over */
}

.modal-small-btn:hover {
    opacity: 0.8;
}

.modal-cancel-btn {
     position: relative;
     border: none; /* Remove borders */
     color: white;
     background-color: #f44336;; /* Add a backgriund color */
     padding: 12px 20px;
     margin: 4px 2px;
     border-radius: 4px;
     left: -15px;
     cursor: pointer; /* Add a pointer cursor on mouse-over */
}

.modal-cancel-btn:hover {
    opacity: 0.8;
}

.modal-label {
    color: black;
    font-family: sans-serif;
    font-size: 18;
    font-weight: bold;
  }

.model-small-button {
    width: 24px;
    height: 24px;
    padding-bottom: 1px;
    border-radius: 50%;
    border: none;
    overflow: hidden;
    background: rgb(69, 89, 102);
  }

  .modal-entry {
     width: 100%; /* Full width */
     height: 20px;
     margin-bottom: 12px;
}

/* Add animation (fade in the popup) */
@-webkit-keyframes fadeIn {
    from {opacity: 0;} 
    to {opacity: 1;}
}

@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity:1 ;}
} 

/* The Close Button */
.close {
    color:white;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    color: #000;
    text-decoration: none;
    cursor: pointer;
}


.sb-headers td {
    background-color: white;
    color: navy;
    padding: 1px;
    font: 12px Trebuchet MS, sans-serif;
}

.sb-cells td {
    font: 10px Trebuchet MS, sans-serif;
    color: rgba(0, 0, 0, 0.6);
}

.sb-headers {
    border-collapse: collapse;
}

.sb-cells {
    border-collapse: collapse;
}

.cells tr td {
    border-top: 1px solid rgba(255, 255, 255, 1.0);
    border-bottom: 1px solid rgba(255, 255, 255, 1.0);
}

.details {
    font: 10px Trebuchet MS, sans-serif;
    color: rgba(0, 0, 0, 0.6);
}

.circle-base {
    border-radius: 50%;
}

.menu-item {
    color: rgba(0, 0, 0, 1.0);
}

.menu-item:hover {
    text-shadow: 0px 0px 2px rgba(0, 0, 0, 0.9);
}

.container::-webkit-scrollbar-track:vertical {
    width: 8px;
    background: rgba(240, 240, 240, 0.05);
    border-radius: 3px;
}

.container::-webkit-scrollbar {
    width: 8px;
    background: rgba(0, 0, 0, 0.0);
    border-radius: 3px;
}

.container::-webkit-scrollbar-track:horizontal {
    height: 8px;
    background: rgba(240, 240, 240, 0.05);
    border-radius: 3px;
}

.container::-webkit-scrollbar {
    width: 8px;
    height: 8px;
    background: rgba(0, 0, 0, 0.0);
    border-radius: 3px;
}

.container::-webkit-scrollbar-thumb {
    border: 1px solid rgb(134, 134, 134);
    background: rgba(0, 0, 0, 0.05);
    border-radius: 3px;
}

.nohighlight:hover {
    background-color: white;
}

.highlight:hover {
    border-top: 1px solid rgba(204, 232, 255, 0.9);
    background-color: rgba(204, 232, 255, 0.6);
    border-bottom: 1px solid rgba(204, 232, 255, 0.9);
}
.fattable-h-scrollbar {
    padding: 0;
    background-color: transparent;
    position: absolute;
    height: auto;
    bottom: 0px;
    left: 0px;
    right: 0px;
    overflow-x: scroll;
    overflow-y: hidden;
}

.fattable-h-scrollbar > div {
    padding: 0 !important;
}

.fattable-v-scrollbar {
    padding: 0;
    position: absolute;
    background-color: transparent;
    width: auto;
    top: 0px;
    bottom: 0px;
    right: 0px;
    overflow-x: hidden;
    overflow-y: scroll;
}

.fattable-v-scrollbar > div {
    padding: 0 !important;
}

* {
    box-sizing: border-box;
    -moz-box-sizing: border-box;
}

.fattable {
    overflow: hidden;
}

.fattable ::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

.fattable ::-webkit-scrollbar-track {
    -webkit-border-radius: 4px;
    background: rgba(240, 240, 240, 0.05);
    border-radius: 4px;
}

.fattable ::-webkit-scrollbar-thumb {
    -webkit-border-radius: 4px;
    border: 1px solid rgb(134, 134, 134);
    background: rgba(0, 0, 0, 0.05);
    border-radius: 4px;
}

.fattable ::-webkit-scrollbar-thumb:hover {
    background: rgba(0, 0, 0, 0.4);
}

.fattable ::-webkit-scrollbar-thumb:window-inactive {
    background: rgba(0, 0, 0, 0.05);
}

.fattable-moving {
    cursor: move;
}

.fattable-viewport {
    overflow: hidden;
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    right: 0;
}

.fattable-viewport > div {
    padding: 2px;
    position: absolute;
    font-size: 10px;
    font-family: sans-serif;
    overflow: hidden;
    text-overflow: ellipsis;
}

.fattable-body-container {
    position: absolute;
    overflow: hidden;
    bottom: 0px;
    width: 100%;
}

.fattable-header-container {
    position: absolute;
    overflow: hidden;
    width: 100%;
    height: 100px;
}

.fattable-header-container .fattable-viewport {
    height: 100%;
}

.fattable-header-container .fattable-viewport > div {
    height: 100%;
}

.fattable-header-container > .fattable-viewport > div {
   font-weight: bold;
   padding-top: 5px;
}
#toolbar {
    height: 42px;
    text-align: left;
    padding: 5px;
    margin-left: 10px;
    margin-right: 10px;
}

#toolbar .layout {
    top: 50%;
    position: relative;
    transform: translateY(-50%);
}

#toolbar .tool {
    padding-right: 5px;
    padding-bottom: 10px;
}

#toolbar h1 {
    padding: 2px 6px;
    font-size: 16px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: white;
    letter-spacing: 4px;
    color: black;
}

#toolbar .tool:last-child {
    padding-right: 0;
}

#toolbar .button {
    width: 32px;
    height: 32px;
    background-color: white;
    background-repeat: no-repeat;
    color: rgba(0, 0, 0, 0.4);
    border: none;
    cursor: pointer;
    overflow: hidden;
    outline: none;
    font-size: 16px;
    margin-right: 4px;
}

#toolbar .button:hover {
    color: rgba(0, 0, 0, 0.8);
}

#toolbar .button:focus {
    outline: 0;
}

#toolbar .button img {
    display: block;
    width: 76%;
    padding: 12%;
    height: auto;
}

#show-tooltip-checkbox-label.disabled {
    color: #888;
}

.graph-container {
    display: flex;
    flex-wrap: wrap;
    align-content: flex-start;
    width: 100%;
    height: 100%;
    justify-content: left;
    box-sizing: border-box;
}

::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    -webkit-border-radius: 4px;
    background: rgba(240, 240, 240, 0.05);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb {
    -webkit-border-radius: 4px;
    border: 1px solid rgb(134, 134, 134);
    background: rgba(0, 0, 0, 0.05);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: rgba(0, 0, 0, 0.4);
}

::-webkit-scrollbar-thumb:window-inactive {
    background: rgba(0, 0, 0, 0.05);
}

</style>

<style>
.checkbox {
    display: block;
    position: relative;
    padding-left: 25;
    margin-bottom: 12px;
    cursor: pointer;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
}
</style>

<script>
function FileUtil(document) {

    this._document = document;

};

FileUtil.prototype.saveAs = function (data, fileName) {
    var saveLink = this._document.createElementNS("http://www.w3.org/1999/xhtml", "a");
    var canUseSaveLink = "download" in saveLink;
    var getURL = function () {
        return view.URL || view.webkitURL || view;
    }

    var click = function (node) {
        var event = new MouseEvent("click");
        node.dispatchEvent(event);
    }

    var fileURL = URL.createObjectURL(new Blob([data], { type: 'text/plain' }));

    saveLink.href = fileURL;
    saveLink.download = fileName;

    click(saveLink);

};

FileUtil.prototype.load = function (callback) {
    var loadButton = this._document.createElementNS("http://www.w3.org/1999/xhtml", "input");

    loadButton.setAttribute("type", "file");

    loadButton.addEventListener('change', function (e) {
        var files = e.target.files

        callback(files);

        return false;

    }, false);

    loadButton.click();

};
</script>
<script>
    'use strict'
    var prefixedTransformCssKey;

    var bound = function(x, m, M) {

        if (x < m) {
            return m;
        } else if (x > M) {
            return M;
        } else {
            return x;
        }

    };

    var smallest_diff_subsequence = function(arr, w) {
        let l = 1;

        let start = 0;

        while (start + l < arr.length) {
            if (arr[start + l] - arr[start] > w) {
                start += 1;

            } else {
                l += 1;
            }

        }

        return l;

    };

    var binary_search = function(arr, x) {
        var a, b, m, v;

        if (arr[0] > x) {
            return 0;
        } else {
            a = 0;
            b = arr.length;

            while (a + 2 < b) {
                m = (a + b) / 2 | 0;
                v = arr[m];

                if (v < x) {
                    a = m;
                } else if (v > x) {
                    b = m;
                } else {
                    return m;
                }
            }
            return a;
        }

    };

    var distance = function(a1, a2) {

        return Math.abs(a2 - a1);

    };

    class Condition {
        constructor() {
            this.callbacks = [];
            this.result = false;
            this.resolved = false;
        }

        then(cb) {

            if (this.resolved) {
                return cb(this.result);
            } else {
                return this.callbacks.push(cb);
            }

        };

        resolve(result) {
            var cb, len, n, ref, results;

            this.resolved = true;
            this.result = result;
            ref = this.callbacks;

            results = [];

            for (n = 0, len = ref.length; n < len; n++) {

                cb = ref[n];

                results.push(cb(result));

            }

            return results;

        }

    }

    var domReadyPromise = new Condition();

    var getTranformPrefix = function() {
        var el, len, n, ref, testKey;

        el = document.createElement("div");

        ref = ["transform", "WebkitTransform", "MozTransform", "OTransform", "MsTransform"];

        for (n = 0, len = ref.length; n < len; n++) {
            testKey = ref[n];

            if (el.style[testKey] !== void 0) {
                return testKey;
            }

        }

    }

    prefixedTransformCssKey = getTranformPrefix();

    class TableModel {

        hasCell(i, j) {

            return false;

        }

        getCell(i, j, callback) {

            callback("getCell not implemented");

        }

        getHeader(j, callback) {

            callback("getHeader not implemented");

        }

    }

    class SyncTableModel extends TableModel {

        getCellSync(i, j) {

            return `[${i}],[${j}]`;

        }

        getHeaderSync(j) {

            return `col [${j}]`;

        }

        hasCell(i, j) {

            return true;

        }

        hasHeader(j) {

            return true;

        }

        getCell(i, j, callback) {

            callback(this.getCellSync(i, j));

        }

        getHeader(j, callback) {

            callback(this.getHeaderSync(j));

        }

    }

    class LRUCache {

        constructor(size = 100) {

            this.__size = size;
            this.__data = {};
            this.__lru_keys = [];

        }

        has(k) {

            return this.__data.hasOwnProperty(k);

        }

        /** 
        * If key k is in the cache, 
        * calls cb immediatly with  as arguments
        *
        * @param {*} k the Key
        *
        */
        get(k) {

            return this.__data[k];

        }

        /**
        * Set a Key
        * 
        * @param {*} k the Key
        * @param {*} v the Value
        */
        set(k, v) {
            var idx = this.__lru_keys.indexOf(k)

            if (idx >= 0) {
                this.__lru_keys.splice(idx, 1);
            }

            this.__lru_keys.push(k);

            if (this.__lru_keys.length >= this.__size) {
                var key = this.__lru_keys.shift();
                delete this.__data[key]
            }

            this.__data[k] = v;

        }

    }

    class PagedAsyncTableModel extends TableModel {

        constructor(cacheSize = 100) {
            this.__pageCache = new LRUCache(cacheSize);
            this.__headerPageCache = new LRUCache(cacheSize);

            this.__fetchCallbacks = {};
            this.__headerFetchCallbacks = {};

        }

        cellPageName(i, j) {
            return "";
        }

        headerPageName(j) {
            return "";
        }

        getHeader(column, callback) {
            var pageName = this.headerPageName(column);

            if (this.__headerPageCache.has(pageName)) {
                return callback(this.__headerPageCache.get(pageName)(column));
            } else if (this.__headerFetchCallbacks[pageName] != null) {
                return this.__headerFetchCallbacks[pageName].push([column, callback]);
            } else {
                this.__headerFetchCallbacks[pageName] = [
                    [column, callback]
                ];

                return this.fetchHeaderPage(pageName, (function(__this) {

                    return function(page) {

                        var cb, len, n, ref, ref1;

                        __this.__headerPageCache.set(pageName, page);

                        ref = __this.__headerFetchCallbacks[pageName];

                        for (n = 0, len = ref.length; n < len; n++) {

                            ref1 = ref[n], column = ref1[0], cb = ref1[1];

                            cb(page(column));

                        }

                        return delete __this.__headerFetchCallbacks[pageName];

                    }

                })(this));

            }

        }

        hasCell(column, row) {
            var pageName = this.cellPageName(column, row);

            return this.__pageCache.has(pageName);

        }

        getCell(i, j, cb) {
            let pageName = this.cellPageName(i, j);

            if (this.pageCache.has(pageName)) {

                return cb(this.__pageCache.get(pageName)(i, j));

            } else if (this.__fetchCallbacks[pageName] != null) {

                return this.__fetchCallbacks[pageName].push([i, j, cb]);

            } else {

                this.__fetchCallbacks[pageName] = [
                    [i, j, cb]
                ];

                return this.__fetchCellPage(pageName, (function(__this) {

                    return function(page) {

                        let len, n, ref, ref1;

                        __this.pageCache.set(pageName, page);

                        ref = _this.fetchCallbacks[pageName];

                        for (let n = 0, len = ref.length; n < len; n++) {

                            ref1 = ref[n], i = ref1[0], j = ref1[1], cb = ref1[2];
                            cb(page(i, j));

                        }

                        return delete __this.fetchCallbacks[pageName];

                    };

                })(this));

            }

        }

        fetchCellPage(pageName, cb) {}

    }

    class Painter {

        setupCell(cellDiv) {}

        setupHeader(headerDiv) {}

        cleanUpCell(cellDiv) {}

        cleanUpHeader(headerDiv) {}

        cleanUp(table) {

            for (let cell in table.cells) {
                this.cleanUpCell(cell)
            }

            for (let header in table.columns) {
                this.cleanUpHeader(header);
            }

        }

        fillHeader(headerDiv, data, column) {

            headerDiv.getElementsByTagName('div')[0].textContent = data;
            headerDiv.getElementsByTagName('div')[0].parentElement.parentElement.style.borderLeft =
                column == 0 ? "1px solid rgb(0,0,0,0.0)" : "1px solid rgb(0,0,0,0.3)";

        }

        fillCell(cellDiv, data) {
            cellDiv.textContent = data;
        }

    }

    class EventRegister {

        constructor() {

            this.boundEvents = [];

        }

        bind(target, event, cb) {
            this.boundEvents.push([target, event, cb]);
            return target.addEventListener(event, cb);
        }

        unbindAll() {
            let cb, event, len, n, ref1, target;

            let ref = this.boundEvents;

            for (n = 0, len = ref.length; n < len; n++) {
                ref1 = ref[n], target = ref1[0], event = ref1[1], cb = ref1[2];
                target.removeEventListener(event, cb);
            }

            return this.boundEvents = [];

        }

    }

    class ScrollBarProxy {

        constructor(container, headerContainer, width, height, eventRegister, visible, enableDragMove) {
            let bigContentHorizontal, bigContentVertical, getDelta, onMouseWheel, onMouseWheelHeader, supportedEvent;

            this.container = container;
            this.headerContainer = headerContainer;
            this.width = width;
            this.height = height;
            this.visible = visible != null ? visible : true;

            this.enableDragMove = enableDragMove != null ? enableDragMove : true;
            this.verticalScrollbar = document.createElement("div");
            this.verticalScrollbar.className += " fattable-v-scrollbar";
            this.horizontalScrollbar = document.createElement("div");
            this.horizontalScrollbar.className += " fattable-h-scrollbar";

            if (this.visible) {
                this.container.appendChild(this.verticalScrollbar);
                this.container.appendChild(this.horizontalScrollbar);
            }

            bigContentHorizontal = document.createElement("div");
            bigContentHorizontal.style.height = 1 + "px";
            bigContentHorizontal.style.width = this.width + "px";
            bigContentVertical = document.createElement("div");
            bigContentVertical.style.width = 1 + "px";
            bigContentVertical.style.height = this.height + "px";

            this.horizontalScrollbar.appendChild(bigContentHorizontal);
            this.verticalScrollbar.appendChild(bigContentVertical);
            this.scrollbarMargin = Math.max(this.horizontalScrollbar.offsetHeight, this.verticalScrollbar.offsetWidth);

            this.verticalScrollbar.style.bottom = this.scrollbarMargin + "px";
            this.horizontalScrollbar.style.right = this.scrollbarMargin + "px";

            this.scrollLeft = 0;
            this.scrollTop = 0;

            this.horizontalScrollbar.onscroll = (function(__this) {

                return function() {

                    if (!__this.dragging) {
                        if (__this.scrollLeft !== __this.horizontalScrollbar.scrollLeft) {
                            __this.scrollLeft = __this.horizontalScrollbar.scrollLeft;

                            if (__this.onScroll != null) {
                                return __this.onScroll(__this.scrollLeft, __this.scrollTop);
                            } else {
                                return;
                            }
                        }

                    }

                };

            })(this);

            this.verticalScrollbar.onscroll = (function(__this) {
                return function() {

                    if (!__this.dragging) {
                        if (__this.scrollTop !== __this.verticalScrollbar.scrollTop) {
                            __this.scrollTop = __this.verticalScrollbar.scrollTop;

                            return __this.onScroll(__this.scrollLeft, __this.scrollTop);

                        }

                    }

                };

            })(this);

            if (this.enableDragMove) {
                eventRegister.bind(this.container, 'mousedown', (function(__this) {

                    return function(event) {
                        if (event.button === 1) {
                            __this.dragging = true;
                            __this.container.className = "fattable-body-container fattable-moving";

                            __this.dragging_dX = __this.scrollLeft + event.clientX;

                            return __this.dragging_dY = __this.scrollTop + event.clientY;

                        }

                    };

                })(this));

                eventRegister.bind(this.container, 'mouseup', (function(__this) {

                    return function(event) {
                        __this.dragging = false;
                        return __this.container.className = "fattable-body-container";
                    };

                })(this));

                eventRegister.bind(this.container, 'mousemove', (function(_this) {
                    return function(event) {
                        let deferred = function() {

                            let newX, newY;

                            if (_this.dragging) {

                                newX = -event.clientX + _this.dragging_dX;
                                newY = -event.clientY + _this.dragging_dY;

                                return _this.setScrollXY(newX, newY);

                            }

                        };

                        return window.setTimeout(deferred, 0);

                    };

                })(this));

                eventRegister.bind(this.container, 'mouseout', (function(__this) {

                    return function(event) {

                        if (__this.dragging) {
                            if ((event.toElement == null) || (event.toElement.parentElement.parentElement !== __this.container)) {
                                __this.container.className = "fattable-body-container";
                                return __this.dragging = false;
                            }
                        }

                    };

                })(this));

                eventRegister.bind(this.headerContainer, 'mousedown', (function(__this) {

                    return function(event) {

                        if (event.button === 1) {
                            __this.headerDragging = true;
                            __this.headerContainer.className = "fattable-header-container fattable-moving";

                            return __this.dragging_dX = __this.scrollLeft + event.clientX;

                        }

                    };

                })(this));

                eventRegister.bind(this.container, 'mouseup', (function(__this) {

                    return function(event) {
                        let captureClick;

                        if (event.button === 1) {
                            __this.headerDragging = false;
                            __this.headerContainer.className = "fattable-header-container";
                            event.stopPropagation();

                            captureClick = function(e) {
                                e.stopPropagation();

                                return __this.removeEventListener('click', captureClick, true);

                            };

                            return __this.container.addEventListener('click', captureClick, true);

                        }

                    };

                })(this));

                eventRegister.bind(this.headerContainer, 'mousemove', (function(__this) {

                    return function(event) {
                        let deferred = function() {
                            var newX;

                            if (__this.headerDragging) {
                                newX = -event.clientX + __this.dragging_dX;

                                return __this.setScrollXY(newX);

                            }

                        };

                        return window.setTimeout(deferred, 0);

                    };

                })(this));

                eventRegister.bind(this.headerContainer, 'mouseout', (function(__this) {

                    return function(event) {

                        if (__this.headerDragging) {

                            if ((event.toElement == null) || (event.toElement.parentElement.parentElement !== __this.headerContainer)) {
                                __this.headerContainer.className = "fattable-header-container";
                            }

                            return __this.headerDragging = false;

                        }

                    };

                })(this));

            }

            if (this.width > this.horizontalScrollbar.clientWidth) {
                this.maxScrollHorizontal = this.width - this.horizontalScrollbar.clientWidth;
            } else {
                this.maxScrollHorizontal = 0;
            }

            if (this.height > this.verticalScrollbar.clientHeight) {
                this.maxScrollVertical = this.height - this.verticalScrollbar.clientHeight;
            } else {
                this.maxScrollVertical = 0;
            }

            supportedEvent = "DOMMouseScroll";

            if (this.container.onwheel !== void 0) {
                supportedEvent = "wheel";
            } else if (this.container.onmousewheel !== void 0) {
                supportedEvent = "mousewheel";
            }

            getDelta = (function() {

                switch (supportedEvent) {

                    case "wheel":

                        return function(event) {
                            let deltaX, deltaY, ref, ref1, ref2, ref3;

                            switch (event.deltaMode) {

                                case event.DOM_DELTA_LINE:
                                    deltaX = (ref = -50 * event.deltaX) != null ? ref : 0;
                                    deltaY = (ref1 = -50 * event.deltaY) != null ? ref1 : 0;

                                    break;

                                case event.DOM_DELTA_PIXEL:
                                    deltaX = (ref2 = -1 * event.deltaX) != null ? ref2 : 0;
                                    deltaY = (ref3 = -1 * event.deltaY) != null ? ref3 : 0;

                            }

                            return [deltaX, deltaY];

                        };

                    case "mousewheel":

                        return function(event) {
                            let ref, ref1;
                            let deltaX = 0;
                            let deltaY = 0;

                            deltaX = (ref = event.wheelDeltaX) != null ? ref : 0;
                            deltaY = (ref1 = event.wheelDeltaY) != null ? ref1 : event.wheelDelta;

                            return [deltaX, deltaY];

                        };

                    case "DOMMouseScroll":

                        return function(event) {
                            let deltaX = 0;
                            let deltaY = 0;

                            if (event.axis === event.HORIZONTAL_AXI) {
                                deltaX = -50.0 * event.detail;
                            } else {
                                deltaY = -50.0 * event.detail;
                            }

                            return [deltaX, deltaY];

                        };

                }

            })();

            onMouseWheel = (function(__this) {

                return function(event) {

                    var deltaX, deltaY, has_scrolled, ref;

                    ref = getDelta(event), deltaX = ref[0], deltaY = ref[1];

                    has_scrolled = __this.setScrollXY(__this.scrollLeft - deltaX, __this.scrollTop - deltaY);

                    if (has_scrolled) {

                        return event.preventDefault();

                    }

                };

            })(this);

            onMouseWheelHeader = (function(__this) {

                return function(event) {

                    var _, deltaX, has_scrolled, ref;

                    ref = getDelta(event), deltaX = ref[0], _ = ref[1];
                    has_scrolled = __this.setScrollXY(__this.scrollLeft - deltaX, __this.scrollTop);

                    if (has_scrolled) {

                        return event.preventDefault();

                    }

                };

            })(this);

            eventRegister.bind(this.container, supportedEvent, onMouseWheel);
            eventRegister.bind(this.headerContainer, supportedEvent, onMouseWheelHeader);

        }

        onScroll(x, y) {

        };

        setScrollXY(x, y) {
            let has_scrolled;

            has_scrolled = false;

            if (x != null) {

                x = bound(x, 0, this.maxScrollHorizontal);

                if (this.scrollLeft !== x) {
                    has_scrolled = true;
                    this.scrollLeft = x;
                }

            } else {
                x = this.scrollLeft;
            }

            if (y != null) {
                y = bound(y, 0, this.maxScrollVertical);

                if (this.scrollTop !== y) {

                    has_scrolled = true;
                    this.scrollTop = y;

                }

            } else {

                y = this.scrollTop;

            }

            this.horizontalScrollbar.scrollLeft = x;
            this.verticalScrollbar.scrollTop = y;
            this.onScroll(x, y);

            return has_scrolled;

        }

    }

    class TableView {

        cumsum(arr) {
            var cs, len, n, s, x;

            cs = [0.0];
            s = 0.0;

            for (n = 0, len = arr.length; n < len; n++) {
                x = arr[n];
                s += x;
                cs.push(s);

            }

            return cs;

        }

        constructor(parameters) {
            let container = parameters.container;

            if (container == null) {
                throw "container not specified.";
            }

            if (typeof container === "string") {
                this.container = document.querySelector(container);
            } else if (typeof container === "object") {
                this.container = container;

            } else {
                throw "Container must be a string or a dom element.";
            }

            this.__processors = [];
            this.current_column = -1;

            this.readRequiredParameter(parameters, "painter", new Painter());
            this.readRequiredParameter(parameters, "autoSetup", true);
            this.readRequiredParameter(parameters, "model");
            this.readRequiredParameter(parameters, "nbRows");
            this.readRequiredParameter(parameters, "rowHeight");
            this.readRequiredParameter(parameters, "columnWidths");
            this.readRequiredParameter(parameters, "rowHeight");
            this.readRequiredParameter(parameters, "headerHeight");
            this.readRequiredParameter(parameters, "scrollBarVisible", true);
            this.readRequiredParameter(parameters, "enableDragMove", true);
            this.nbCols = this.columnWidths.length;

            if ((" " + this.container.className + " ").search(/\sfattable\s/) === -1) {
                this.container.className += " fattable";
            }

            this.height = this.rowHeight * this.nbRows;
            this.columnOffset = this.cumsum(this.columnWidths);
            this.width = this.columnOffset[this.columnOffset.length - 1];

            this.columns = {};
            this.cells = {};
            this.currentColumn = null;

            this.getContainerDimension();

            this.eventRegister = new EventRegister();

            this.eventRegister.bind(window, 'resize', (function(__this) {

                return function(event) {
                     __this.resize();
                };

            })(this));

            this.eventRegister.bind(document, 'mouseup', (function(__this) {

                return function(event) {

                    __this.currentColumn = null;

                };

            })(this));

            if (this.autoSetup) {

                domReadyPromise.then((function(__this) {

                    return function() {

                        return __this.setup();

                    };

                })(this));

            }

        }

        readRequiredParameter(parameters, k, default_value) {

            if (parameters[k] == null) {

                if (default_value === void 0) {
                    throw `Expected parameter <${k}>`;
                } else {
                    return this[k] = default_value;
                }

            } else {
                return this[k] = parameters[k];
            }

        };

        getContainerDimension() {
            this.w = this.container.offsetWidth;
            this.h = this.container.offsetHeight - this.headerHeight;
            this.nbColsVisible = Math.min(smallest_diff_subsequence(this.columnOffset, this.w) + 2, this.columnWidths.length);
            this.nbRowsVisible = Math.min((this.h / this.rowHeight | 0) + 2, this.nbRows);

        };

        leftTopCornerFromXY(x, y) {

            let i = bound(y / this.rowHeight | 0, 0, this.nbRows - this.nbRowsVisible);
            let j = bound(binary_search(this.columnOffset, x), 0, this.nbCols - this.nbColsVisible);

            return [i, j];

        };

        cleanUp() {
            var ref;

            if ((ref = this.scroll) != null) {

                ref.onScroll = null;

            }

            this.painter.cleanUp(this);
            this.container.innerHTML = "";

            this.bodyContainer = null;

            return this.headerContainer = null;

        };

        setup() {
            var iColumn, row, column, n, o, onScroll, p, ref, ref1, ref2, ref3, ref4, ref5;

            this.cleanUp();
            this.getContainerDimension();
            this.columns = {};
            this.cells = {};

            this.container.innerHTML = "";
            this.headerContainer = document.createElement("div");
            this.headerContainer.className += " fattable-header-container";

            this.headerContainer.style.height = this.headerHeight + "px";
            this.headerViewport = document.createElement("div");
            this.headerViewport.className = "fattable-viewport";
            this.headerViewport.style.width = this.width + "px";
            this.headerViewport.style.height = this.headerHeight + "px";

            this.headerContainer.appendChild(this.headerViewport);

            this.bodyContainer = document.createElement("div");
            this.bodyContainer.className = "fattable-body-container";
            this.bodyContainer.style.top = this.headerHeight + "px";

            this.bodyViewport = document.createElement("div");
            this.bodyViewport.className = "fattable-viewport";
            this.bodyViewport.style.width = this.width + "px";

            this.bodyViewport.style.height = this.height + "px";
            let __self = this;

            for (column = n = ref = this.nbColsVisible, ref1 = this.nbColsVisible * 2; n < ref1; column = n += 1) {

                for (row = o = ref2 = this.nbRowsVisible, ref3 = this.nbRowsVisible * 2; o < ref3; row = o += 1) {
                    let element = document.createElement("div");

                    this.painter.setupCell(element);
                    element.pending = false;
                    element.style.height = this.rowHeight + "px";

                    element.style.textOverflow = "ellipsis";
                    element.style.whiteSpace = "nowrap"
                    element.style.overflow = "none";

                    this.bodyViewport.appendChild(element);
                    this.cells[`${row},${column}`] = element;

                    element.onmouseover = function(e) {
                        var coordinates = /(\d*),(\d*)/.exec(element.getAttribute("id"));

                        for (var iColumn = __self.firstVisibleColumn; iColumn < __self.firstVisibleColumn + __self.nbColsVisible; iColumn++) {
                            __self.cells[`${coordinates[1]},${iColumn}`].style.backgroundColor = "rgba(0,0,0,0.1)";
                        }

                    }

                    element.onmouseout = function(e) {
                        var coordinates = /(\d*),(\d*)/.exec(element.getAttribute("id"));

                        for (var iColumn = __self.firstVisibleColumn; iColumn < __self.firstVisibleColumn + __self.nbColsVisible; iColumn++) {
                            __self.cells[`${coordinates[1]},${iColumn}`].style.backgroundColor = "white";
                        }
                    }

                    element.onmousedown = function(e) {
                        var coordinates = /(\d*),(\d*)/.exec(element.getAttribute("id"));

                        for (let processor in __self.__processors) {

                            __self.__processors[processor](coordinates[1]);

                        }

                    }

                }

            }

            for (iColumn = p = ref4 = this.nbColsVisible, ref5 = this.nbColsVisible * 2; p < ref5; iColumn = p += 1) {
                var element = document.createElement("div");
                var span = document.createElement("span");

                element.style.borderLeft = "1px solid rgb(0,0,0,0.0)";
                element.style.height = this.headerHeight + "px";
                element.pending = false;

                var text = document.createElement("div");

                text.style.height = this.headerHeight + "px";
                text.style.position = "absolute";
                text.style.textOverflow = "ellipsis";
                text.style.whiteSpace = "nowrap";
                text.style.overflow = "hidden";
                text.style.left = "2px";
                text.style.top = "6px";

                text.textContent = "";

                span.appendChild(text);

                var divider = document.createElement("div");

                divider.style.width = "2px";
                divider.style.height = this.headerHeight + "px";
                divider.style.position = "absolute";
                divider.style.right = "1px";
                divider.style.cursor = "col-resize";
                divider.id = `divider-${iColumn}`;

                var eventRegister = new EventRegister();

                eventRegister.bind(divider, 'mousedown', (function(params) {

                    return function(event) {
                        params.owner.currentColumn = params.element;
                    };

                })({
                    owner: this,
                    element: element,
                }));

                span.appendChild(divider);

                this.painter.setupHeader(element);

                element.id = `column-${iColumn}`;

                this.columns[iColumn] = element;

                element.appendChild(span);

                this.headerViewport.appendChild(element);

            }

            this.firstVisibleRow = this.nbRowsVisible;
            this.firstVisibleColumn = this.nbColsVisible;
            this.display(0, 0);

            this.container.appendChild(this.bodyContainer);
            this.container.appendChild(this.headerContainer);
            this.bodyContainer.appendChild(this.bodyViewport);

            this.refreshAllContent();

            this.scroll = new ScrollBarProxy(this.bodyContainer, this.headerContainer, this.width, this.height,
                this.eventRegister, this.scrollBarVisible, this.enableDragMove);

            onScroll = (function(__this) {

                return function(x, y) {
                    var _, cell, col, ref6, ref7, cellRef;

                    ref6 = __this.leftTopCornerFromXY(x, y), row = ref6[0], column = ref6[1];

                    __this.display(row, column);

                    ref7 = __this.columns;

                    for (_ in ref7) {

                        col = ref7[_];
                        col.style[prefixedTransformCssKey] = "translate(" + (col.left - x) + "px, 0px)";

                    }

                    cellRef = __this.cells;

                    for (_ in cellRef) {
                        cell = cellRef[_];
                        cell.style[prefixedTransformCssKey] = "translate(" + (cell.left - x) + "px," + (cell.top - y) + "px)";

                    }

                    clearTimeout(__this.scrollEndTimer);
                    __this.scrollEndTimer = setTimeout(__this.refreshAllContent.bind(__this), 200);

                    return __this.onScroll(x, y);

                };

            })(this);

            this.eventRegister.bind(document, 'mousemove', (function(__this) {

                return function(event) {

                    if (__this.currentColumn != null) {
                        var rect = __this.currentColumn.getBoundingClientRect();
                        var width = event.pageX - Math.round(rect.left);
                        var styleWidth = parseInt(__this.currentColumn.style.width.replace('px', ''));

                        if (width < 10) {
                            return;
                        }

                        var diff = width - styleWidth;

                        var nextColumn = false;
                        var left = __this.columns[__this.firstVisibleColumn].left;
                        var columnPos = __this.firstVisibleColumn;
                        var nextWidth = 0;
                        var leftPosition = 0;
                        var widths = [];

                        for (var iColumn = __this.firstVisibleColumn; iColumn < __this.nbColsVisible + __this.firstVisibleColumn; iColumn += 1) {
                            var nextRect = __this.columns[iColumn].getBoundingClientRect();

                            if (nextColumn) {
                                var columnWidth = parseInt(__this.columns[iColumn].style.width.replace('px', '')) - diff;

                                if (columnWidth < 10) {
                                    return;
                                }

                                __this.currentColumn.style.width = `${width}px`;
                                __this.columns[columnPos].style[prefixedTransformCssKey] = `translate(${(left - __this.scroll.scrollLeft)}px, 0px)`;

                                __this.columns[columnPos].left = left;
                                __this.columnOffset[columnPos] = left - diff;
                                __this.columnWidths[columnPos] = columnWidth;
                                __this.columns[columnPos].style.width = `${columnWidth}px`;

                                leftPosition = left;
                                left += columnWidth;

                                widths.push(columnWidth);

                                nextColumn = false;

                            } else if (__this.columns[iColumn].id == __this.currentColumn.id) {
                                __this.columnWidths[columnPos] = width;
                                columnPos = iColumn;
                                widths.push(width);

                                left += width;

                                nextColumn = true;
                            } else {
                                left += parseInt(__this.columns[iColumn].style.width.replace('px', ''));
                            }

                            columnPos = columnPos + 1;

                        }

                        nextColumn = false;

                        for (var iRow = __this.firstVisibleRow; iRow < __this.nbRowsVisible + __this.firstVisibleRow; iRow += 1) {
                            for (var iColumn = __this.firstVisibleColumn; iColumn < __this.nbColsVisible + __this.firstVisibleColumn; iColumn += 1) {
                                var k = iRow + "," + iColumn;

                                if (nextColumn) {
                                    __this.cells[k].style.width = `${widths[1]}px`;
                                    __this.cells[k].left = leftPosition;
                                    __this.cells[k].style[prefixedTransformCssKey] = `translate(${leftPosition - __this.scroll.scrollLeft}px, ${(iRow * __this.rowHeight) - __this.scroll.scrollTop}px)`;

                                    nextColumn = false;

                                }

                                if (__this.columns[iColumn].id == __this.currentColumn.id) {
                                    __this.cells[k].style.width = `${widths[0]}px`;
                                    nextColumn = true;
                                }

                            }

                        }

                    }

                };

            })(this));

            this.scroll.onScroll = onScroll;

            return onScroll(0, 0);

        }

        resize() {
            var last_i = this.firstVisibleRow;
            var last_j = this.scroll.scrollLeft;

            this.setup();

            var targetY = this.rowHeight * last_i;

            return this.scroll.setScrollXY(last_j, targetY);

        }

        refreshAllContent(evenNotPending) {
            var cell, drawer, header, row, column, k, n, ref, ref1, results;

            if (evenNotPending == null) {

                evenNotPending = false;

            }

            drawer = (function(__this) {

                return function(header, column) {

                    if (evenNotPending || header.pending) {

                        return __this.model.getHeader(column, function(data) {

                            header.pending = false;

                            return __this.painter.fillHeader(header, data, column);

                        });

                    }

                };

            })(this);

            results = [];

            for (column = n = ref = this.firstVisibleColumn, ref1 = this.firstVisibleColumn + this.nbColsVisible; n < ref1; column = n += 1) {

                header = this.columns[column];

                drawer(header, column);

                results.push((function() {
                    var tracker, ref2, ref3, rows;

                    rows = [];

                    for (row = tracker = ref2 = this.firstVisibleRow, ref3 = this.firstVisibleRow + this.nbRowsVisible; tracker < ref3; row = tracker += 1) {

                        k = row + "," + column;

                        cell = this.cells[k];

                        if (evenNotPending || cell.pending) {

                            rows.push((function(__this) {

                                return function(cell) {

                                    return __this.model.getCell(row, column, function(data) {

                                        cell.pending = false;

                                        return __this.painter.fillCell(cell, data);

                                    });

                                };

                            })(this)(cell));

                        } else {

                            rows.push(void 0);

                        }

                    }

                    return rows;

                }).call(this));

            }

            return results;

        };

        onScroll(x, y) {};

        goTo(i, j) {
            var targetX, targetY;

            targetY = i != null ? this.rowHeight * i : void 0;
            targetX = j != null ? this.columnOffset[j] : void 0;

            return this.scroll.setScrollXY(targetX, targetY);

        };

        display(i, j) {

            this.headerContainer.style.display = "none";
            this.bodyContainer.style.display = "none";

            this.moveX(j);
            this.moveY(i);

            this.headerContainer.style.display = "";
            return this.bodyContainer.style.display = "";

        };

        moveX(j) {
            var cell, col_width, col_x, column, dj, fn, header, i, k, last_i, last_j, n, o, offset_j, orig_j, ref, ref1, ref2, shift_j;

            last_i = this.firstVisibleRow;
            last_j = this.firstVisibleColumn;

            shift_j = j - last_j;

            if (shift_j === 0) {

                return;

            }

            dj = Math.min(Math.abs(shift_j), this.nbColsVisible);

            for (offset_j = n = 0, ref = dj; n < ref; offset_j = n += 1) {

                if (shift_j > 0) {
                    orig_j = this.firstVisibleColumn + offset_j;
                    column = j + offset_j + this.nbColsVisible - dj;

                } else {
                    orig_j = this.firstVisibleColumn + this.nbColsVisible - dj + offset_j;
                    column = j + offset_j;

                }

                col_x = this.columnOffset[column];

                col_width = this.columnWidths[column] + "px";

                header = this.columns[orig_j];

                delete this.columns[orig_j];

                if (this.model.hasHeader(column)) {

                    this.model.getHeader(column, (function(__this) {

                        return function(data) {

                            header.pending = false;

                            return __this.painter.fillHeader(header, data, column);

                        };

                    })(this));

                }

                header.left = col_x;

                header.style.width = col_width;

                this.columns[column] = header;

                fn = (function(__this) {

                    return function(cell) {

                        if (__this.model.hasCell(i, column)) {

                            return __this.model.getCell(i, column, function(data) {

                                cell.pending = false;

                                return __this.painter.fillCell(cell, data);

                            });

                        }

                    };

                })(this);

                for (i = o = ref1 = last_i, ref2 = last_i + this.nbRowsVisible; o < ref2; i = o += 1) {

                    k = i + "," + orig_j;

                    cell = this.cells[k];
                    delete this.cells[k];

                    this.cells[i + "," + column] = cell;
                    cell.left = col_x;
                    cell.style.width = col_width;

                    fn(cell);

                }

            }

            return this.firstVisibleColumn = j;

        }

        moveY(i) {
            var cell, dest_i, di, fn, j, k, last_i, last_j, n, o, offset_i, orig_i, ref, ref1, ref2, row_y, shift_i;

            last_i = this.firstVisibleRow;
            last_j = this.firstVisibleColumn;

            shift_i = i - last_i;

            if (shift_i === 0) {

                return;

            }

            di = Math.min(Math.abs(shift_i), this.nbRowsVisible);

            for (offset_i = n = 0, ref = di; n < ref; offset_i = n += 1) {

                if (shift_i > 0) {
                    orig_i = last_i + offset_i;
                    dest_i = i + offset_i + this.nbRowsVisible - di;

                } else {
                    orig_i = last_i + this.nbRowsVisible - di + offset_i;
                    dest_i = i + offset_i;
                }

                row_y = dest_i * this.rowHeight;

                fn = (function(__this) {

                    return function(cell) {
                        cell.setAttribute("id", `${dest_i},${j}`);

                        if (__this.model.hasCell(dest_i, j)) {

                            return __this.model.getCell(dest_i, j, function(data) {

                                cell.pending = false;

                                return __this.painter.fillCell(cell, data);

                            });

                        }

                    };

                })(this);

                for (j = o = ref1 = last_j, ref2 = last_j + this.nbColsVisible; o < ref2; j = o += 1) {

                    k = orig_i + "," + j;

                    cell = this.cells[k];
                    delete this.cells[k];

                    this.cells[dest_i + "," + j] = cell;

                    cell.top = row_y;

                    fn(cell);

                }

            }

            return this.firstVisibleRow = i;

        }

        get processors() {
            return this.__processors;
        }

        set processors(processors) {
            return this.__processors = processors;
        }

        addProcessor(processor) {
            this.__processors.push(processor);
        }

    }
</script>
<script>
var xOffset = 20;
var yOffset = 16;

var rows = [];
var columns = null;
var categorical = [];
var continuous = [];
var currentRow = 0;
var currentView = 0;

var detailsTableHeight = 0;
var tableView = null;

class DataView extends SyncTableModel {

    constructor(columns, data, types) {
        super();

        this.__columns = columns;
        this.__data = data;
        this.__records = data.length;
        this.__types = types;
        
    }

    get Length() {
        return this.__records;
    }

    getCellSync(i, j, cb) {

        return this.__data[i][j];

    }

    getHeaderSync(j) {

        return this.__columns[j];

    };

    hasCell(i, j) {

        return i < this.__data.length && j < this.__columns.length;

    }

    toJSON() {
        let json = {
            columns : this.__columns,
            data: this.__data,
            types: this.__types
        }

        return json;

    }

}

function resize() {}

function hexbin() {
    function process_hexbin(dataview) {
        let json = dataview.toJSON();

        json['row'] = currentRow;

        show_hexbin(JSON.stringify(json), hexbin_callback);
    }
    
    function hexbin_callback(value) {
        let plots = JSON.parse(value);

        var html = `<div style="margin: 0 auto; margin-top: 6px; text-align:left; overflow:hidden;">` +
                    `<label id="row-hex" style="color:navy; font-size:12px; height:16px; width:30px; line-height:36px; margin-left:5px; ">` +
                    `Row: ${parseInt(currentRow) + 1}</label></div>`;
            
        html += `<div style="position:absolute; margin-top:5px; left:0px; right:0px; height:1px; background-color:rgba(0,0,0,0.2); overflow:hidden;"></div>`;
        html +=  `<div style="position:absolute; width:100%; top:50px; bottom:0px;">`;

        html += `<div class="graph-container" style="position:absolute; overflow:auto;">`;

        for (var plot in plots) {
            html += `<div style="margin-left:20px">`;
            html += `<img src="data:image/png;base64,${plots[plot]['plot']}"></img>`;
            html += `</div>`;
        }

        html += `</div>`;
        html += `</div>`;

        document.getElementById('hexbin').innerHTML = html;

        document.getElementById('waitDialog').style.display = "none";
        document.getElementById('details').style.display = "none";
        document.getElementById('plots').style.display = "none";
        document.getElementById('hexbin').style.display = "inline-block";
        document.getElementById('boxplot').style.display = "none";
        document.getElementById('hist').style.display = "none";
 
    }

    process_hexbin(dataview);

}

function boxplot() {
    function process_boxplot(dataview) {
        let json = dataview.toJSON();

        json['row'] = currentRow;

        show_boxplot(JSON.stringify(json), boxplot_callback);
    }
    
    function boxplot_callback(value) {
        let plots = JSON.parse(value);

        var html = `<div style="margin: 0 auto; margin-top: 6px; text-align:left; overflow:hidden;">` +
                    `<label id="row-box" style="color:navy; font-size:12px; height:16px; width:30px; line-height:36px; margin-left:5px; ">` +
                    `Row: ${parseInt(currentRow) + 1}</label></div>`;
            
        html += `<div style="position:absolute; margin-top:5px; left:0px; right:0px; height:1px; background-color:rgba(0,0,0,0.2); overflow:hidden;"></div>`;
        html +=  `<div style="position:absolute; width:100%; top:50px; bottom:0px;">`;

        html += `<div class="graph-container" style="position:absolute; overflow:auto;">`;

        for (var plot in plots) {
            html += `<div style="margin-left:20px">`;
            html += `<img src="data:image/png;base64,${plots[plot]['plot']}"></img>`;
            html += `</div>`;
        }

        html += `</div>`;
        html += `</div>`;

        document.getElementById('boxplot').innerHTML = html;

        document.getElementById('waitDialog').style.display = "none";
        document.getElementById('details').style.display = "none";
        document.getElementById('plots').style.display = "none";
        document.getElementById('hexbin').style.display = "none";
        document.getElementById('boxplot').style.display = "inline-block";
        document.getElementById('hist').style.display = "none";
 
    }

    process_boxplot(dataview);

}

function hist() {
    function process_hist(dataview) {
        let json = dataview.toJSON();

        json['row'] = currentRow;

        show_hist(JSON.stringify(json), hist_callback);
    }
    
    function hist_callback(value) {
        let plots = JSON.parse(value);

        var html = `<div style="margin: 0 auto; margin-top: 6px; text-align:left; overflow:hidden;">` +
                    `<label id="row-hist" style="color:navy; font-size:12px; height:16px; width:30px; line-height:36px; margin-left:5px; ">` +
                    `Row: ${parseInt(currentRow) + 1}</label></div>`;
            
        html += `<div style="position:absolute; margin-top:5px; left:0px; right:0px; height:1px; background-color:rgba(0,0,0,0.2); overflow:hidden;"></div>`;
        html +=  `<div style="position:absolute; width:100%; top:50px; bottom:0px;">`;

        html += `<div class="graph-container" style="position:absolute; overflow:auto;">`;

        for (var plot in plots) {
            html += `<div style="margin-left:20px">`;
            html += `<img src="data:image/png;base64,${plots[plot]['plot']}"></img>`;
            html += `</div>`;
        }

        html += `</div>`;
        html += `</div>`;

        document.getElementById('hist').innerHTML = html;

        document.getElementById('waitDialog').style.display = "none";
        document.getElementById('details').style.display = "none";
        document.getElementById('plots').style.display = "none";
        document.getElementById('hexbin').style.display = "none";
        document.getElementById('boxplot').style.display = "none";
        document.getElementById('hist').style.display = "inline-block";
 
    }

    process_hist(dataview);

}

function plot() {
    function process_plot(dataview) {
        let json = dataview.toJSON();

        json['row'] = currentRow;

        show_plot(JSON.stringify(json), plot_callback);
    }
    
    function plot_callback(value) {
        let plots = JSON.parse(value);

        var html = `<div style="margin: 0 auto; margin-top: 6px; text-align:left; overflow:hidden;">` +
                    `<label id="row-plot" style="color:navy; font-size:12px; height:16px; width:30px; line-height:36px; margin-left:5px; ">` +
                    `Row: ${parseInt(currentRow) + 1}</label></div>`;
            
        html += `<div style="position:absolute; margin-top:5px; left:0px; right:0px; height:1px; background-color:rgba(0,0,0,0.2); overflow:hidden;"></div>`;
        html +=  `<div style="position:absolute; width:100%; top:50px; bottom:0px;">`;

        html += `<div class="graph-container" style="position:absolute; overflow:auto;">`;

        for (var plot in plots) {
            html += `<div style="margin-left:20px">`;
            html += `<img src="data:image/png;base64,${plots[plot]['plot']}"></img>`;
            html += `</div>`;
        }

        html += `</div>`;
        html += `</div>`;

        document.getElementById('plots').innerHTML = html;

        document.getElementById('waitDialog').style.display = "none";
        document.getElementById('details').style.display = "none";
        document.getElementById('hexbin').style.display = "none";
        document.getElementById('plots').style.display = "inline-block";
        document.getElementById('boxplot').style.display = "none";
        document.getElementById('hist').style.display = "none";
 
    }

    process_plot(dataview);

}

function details() {
    function summary(heading, columns, variables, row) {
        var html = "";

        if (variables.length > 0) {
            html += `<fieldset style="margin-top:5px;"><legend>${heading}</legend>`;
            html += `<table style="margin:0px;">`;

            for (var variable in variables) {
                html += `<tr><td><label ` +
                        `style="width:100px; text-overflow: ellipsis; color:navy; white-space:nowrap; overflow:hidden; display:inline-block;">` +
                        `${columns[variables[variable]]}</label></td><td>${row == null ? '-' : row[variables[variable]]}</td></tr>`;
            }

            html += `</table>`;
            html += `</fieldset>`;

        }

        return html;

    }

    var position = currentRow == null ? '&#x2756;' : parseInt(currentRow) + 1;

    let html = "";

    html += `<div style="margin: 0 auto; margin-top: 6px; text-align:left; overflow:hidden;">` +
    `<label id="row-details" style="color:navy; font-size:12px; height:16px; width:30px; line-height:36px; margin-left:5px; ">` +
    `Row: ${position}</label></div>`;

    html += `<div style="position:absolute; margin-top:5px; left:0px; right:0px; height:1px; background-color:rgba(0,0,0,0.2); overflow:hidden;"></div>`;

    html += `<div style="position:absolute; margin-top:0px; left:0px; right:0px; top:50px; bottom:0px; style="overflow:hidden;">` +
            `<div id="details-container" class="container" style="overflow-y: auto; overflow-x: auto; position:absolute; width:100%; bottom:5px; top:0px;">`;

    html += summary("Categorical", columns, categorical, currentRow == null ? null : rows[currentRow]);
    html += summary("Continuous", columns, continuous, currentRow == null  ? null : rows[currentRow]);

    html += `</div></div>`;

    document.getElementById('details').innerHTML = html;

}

function open() {
         
    document.addEventListener('dragover', event => event.preventDefault());
    document.addEventListener('drop', event => event.preventDefault());

    let fileutil = new FileUtil(document);

    fileutil.load((files) => {
        Array.prototype.slice.call(files).forEach((file) => {
            let reader = new FileReader();

            reader.onload = (e) => {

                    document.getElementById('waitDialog').style.display = "inline-block";
                    document.getElementById('placeholder').style.display = "none";
 
                    window.setTimeout(function() {

                        function process_result(value) {
                            process_file(value, result_callback);
                        }

                        function result_callback(value) {
                            function show(row) {
                                currentRow = row;

                                if (currentView == 0) {
                                    details();
                                } else if (currentView == 1) {
 
                                    document.getElementById('waitDialog').style.display = "inline-block";

                                    window.setTimeout(function() {
                                       plot();
                                    }, 10);

                                } else if (currentView == 2) {
 
                                    document.getElementById('waitDialog').style.display = "inline-block";

                                    window.setTimeout(function() {
                                        hexbin();
                                    }, 10);

                                } else if (currentView == 3) {
 
                                    document.getElementById('waitDialog').style.display = "inline-block";

                                    window.setTimeout(function() {
                                        boxplot();
                                    }, 10);

                                } else if (currentView == 4) {
 
                                    document.getElementById('waitDialog').style.display = "inline-block";

                                    window.setTimeout(function() {
                                        hist();
                                    }, 10);

                                }

                            }

                            let results = JSON.parse(value);

                            rows = results.rows;
                            columns = results.columns;
                            types = results.types;
  
                            document.getElementById('details').innerHTML = "";

                            let widths = [];

                            for (var iColumn in columns) {
                                widths.push(300);
                            }

                            let node = document.getElementById('table');
                            while (node.hasChildNodes()) {
                                node.removeChild(node.lastChild);
                            }

                            dataview = new DataView(columns, rows, types);
                            let painter = new Painter();

                            tableView = new TableView({
                                "container": "#table",
                                "model": dataview,
                                "nbRows": dataview.Length,
                                "rowHeight": 20,
                                "headerHeight": 20,
                                "painter": painter,
                                "columnWidths": widths
                            });

                            tableView.addProcessor(function(row) {
                                show(row);
                            })

                            continuous = [];
                            categorical = [];

                            for (var datatype in types) {

                                if (types[datatype] == 'string') {
                                    categorical.push(datatype); 
                                } else {
                                    continuous.push(datatype); 
                                }
                            }

                            currentRow = rows.length == 0 ? null : 0;
                            show(currentRow);
   
                            window.setTimeout(function() {
                                document.getElementById('waitDialog').style.display = "none";    
                                document.getElementById('table').style.display = "inline-block";
                                
                                tableView.setup();
                                tableView.resize();
                            }, 10);

                        }

                        process_result(reader.result);

                    }, 100);

                },

                reader.readAsText(file);

        });

    });

}

/**
 * Respond to the Document 'ready' event
 */
 window.onload = function() {

    window.addEventListener('resize', (e) => {});

    document.getElementById('upload').addEventListener('click', (e) => {

       open();

        return false;

    });

    document.getElementById('open').addEventListener('click', (e) => {

        open();

        return false;

    });

    document.getElementById('listview').addEventListener('click', (e) => {

        currentView = 0;

        document.getElementById('listview').style.color = "rgba(0,0,0,1.0)";
        document.getElementById('scatterplotview').style.color = "rgba(110,110,110,1.0)";
        document.getElementById('hexplotview').style.color = "rgba(110,110,110,1.0)";
        document.getElementById('boxplotview').style.color = "rgba(110,110,110,1.0)";
        document.getElementById('histplotview').style.color = "rgba(110,110,110,1.0)";
  
        document.getElementById('details').style.display = "inline-block";
        document.getElementById('plots').style.display = "none";
        document.getElementById('hexbin').style.display = "none";
        document.getElementById('boxplot').style.display = "none";
        document.getElementById('hist').style.display = "none";
  
        details();

        return false;

    });

    document.getElementById('scatterplotview').addEventListener('click', (e) => {

        currentView = 1;

        document.getElementById('listview').style.color = "rgba(110,110,110,1.0)";
        document.getElementById('scatterplotview').style.color = "rgba(0,0,0,1.0)";
        document.getElementById('hexplotview').style.color = "rgba(110,110,110,1.0)";
        document.getElementById('boxplotview').style.color = "rgba(110,110,110,1.0)";
        document.getElementById('histplotview').style.color = "rgba(110,110,110,1.0)";
       
        var rowId = document.getElementById('row-plot')
        var position = rowId == null ? - 1  : parseInt(rowId.innerHTML.replace("Row: ",""))  - 1;

        if (position != currentRow) {
            document.getElementById('waitDialog').style.display = "inline-block";
            window.setTimeout(function() {
                plot();
            }, 10);

        } else {
            document.getElementById('details').style.display = "none";
            document.getElementById('plots').style.display = "inline-block";
            document.getElementById('hexbin').style.display = "none";
            document.getElementById('boxplot').style.display = "none";
            document.getElementById('hist').style.display = "none";
        }

        return false;

    });
    
    document.getElementById('hexplotview').addEventListener('click', (e) => {

        currentView = 2;

        document.getElementById('listview').style.color = "rgba(110,110,110,1.0)";
        document.getElementById('scatterplotview').style.color = "rgba(110,110,110,1.0)";
        document.getElementById('hexplotview').style.color = "rgba(0,0,0,1.0)";
        document.getElementById('boxplotview').style.color = "rgba(110,110,110,1.0)";
        document.getElementById('histplotview').style.color = "rgba(110,110,110,1.0)";
       
        var rowId = document.getElementById('row-hex')
        var position = rowId == null ? - 1  : parseInt(rowId.innerHTML.replace("Row: ",""))  - 1;

        if (position != currentRow) {
            document.getElementById('waitDialog').style.display = "inline-block";
            window.setTimeout(function() {
                hexbin();
            }, 10);

        } else {
            document.getElementById('details').style.display = "none";
            document.getElementById('plots').style.display = "none";
            document.getElementById('hexbin').style.display = "inline-block";
            document.getElementById('boxplot').style.display = "none";
            document.getElementById('hist').style.display = "none";
        }

        return false;

    });

    document.getElementById('boxplotview').addEventListener('click', (e) => {

        currentView = 3;

        document.getElementById('listview').style.color = "rgba(110,110,110,1.0)";
        document.getElementById('scatterplotview').style.color = "rgba(110,110,110,1.0)";
        document.getElementById('hexplotview').style.color = "rgba(110,110,110,1.0)";
        document.getElementById('boxplotview').style.color = "rgba(0,0,0,1.0)";
        document.getElementById('histplotview').style.color = "rgba(110,110,110,1.0)";
          
        var rowId = document.getElementById('row-box')
        var position = rowId == null ? - 1  : parseInt(rowId.innerHTML.replace("Row: ",""))  - 1;

        if (position != currentRow) {
            document.getElementById('waitDialog').style.display = "inline-block";
            window.setTimeout(function() {
                boxplot();
            }, 10);

        } else {
            document.getElementById('details').style.display = "none";
            document.getElementById('plots').style.display = "none";
            document.getElementById('hexbin').style.display = "none";
            document.getElementById('boxplot').style.display = "inline-block";
            document.getElementById('hist').style.display = "none";
        }

        return false;

    });

    document.getElementById('histplotview').addEventListener('click', (e) => {

        currentView = 4;

        document.getElementById('listview').style.color = "rgba(110,110,110,1.0)";
        document.getElementById('scatterplotview').style.color = "rgba(110,110,110,1.0)";
        document.getElementById('hexplotview').style.color = "rgba(110,110,110,1.0)";
        document.getElementById('boxplotview').style.color = "rgba(110,110,110,1.0)";
        document.getElementById('histplotview').style.color = "rgba(0,0,0,1.0)";
          
        var rowId = document.getElementById('row-hist')
        var position = rowId == null ? - 1  : parseInt(rowId.innerHTML.replace("Row: ",""))  - 1;

        if (position != currentRow) {
            document.getElementById('waitDialog').style.display = "inline-block";
            window.setTimeout(function() {
                hist();
            }, 10);

        } else {
            document.getElementById('details').style.display = "none";
            document.getElementById('plots').style.display = "none";
            document.getElementById('hexbin').style.display = "none";
            document.getElementById('boxplot').style.display = "none";
            document.getElementById('hist').style.display = "inline-block";
        }

        return false;

    });

}
</script>
</head>

<body>
    <div id="waitDialog" class="modal">
        <div style="position:fixed; width:100%; height:100%;">
            <div style="position:absolute; left: 50%; top: 40%; font:12px Trebuchet MS, sans-serif;">
                <span style="width:12px;height:12px;">
                    &#9203;                
                </span>
                <label>Loading...</label>
            </div>
        </div>
    </div>

    <div style="overflow:hidden; user-select: none;">
        <div style="overflow:hidden;">

            <div id="toolbar" style="position: absolute; top:0px; left:0px; right:0px; height:36px;">
                <div style="position: absolute; top:-2px; left:0px; font-size:24px; padding-right:0px;">
                   &#x1F47B;
                </div>
                <div style="position: absolute; top:-8px; left:36px; padding-right:0px;">
                    <h1>Prattle - CSV Viewer</h1>
                </div>

                <div style="position:absolute; top:2px; right:2px; width:35px;">
                    <a id="open" style="position:absolute; font-size:18px; left:6px;" class="menu-item">&#x1F575;</a>
                </div>

            </div>

            <div id="container" style="position:absolute; top:32px; left:10px; right:340px; bottom:10px; border: 1px solid rgba(0,0,0, 0.2); overflow:hidden;">
                <div id="placeholder" style="position:absolute; display:inline-block; top:10px; left:10px; right:10px; bottom:10px">
                    <div id="upload" class="menu-item" style="color: rgba(0,0,0,0.1); margin-left:45%; margin-top:20%; font-size:128px;">
                        &#x1F575;
                    </div>
                </div>
                <div id="table" style="position:absolute; display:none; left:2px; top:2px; bottom:2px; right:2px; overflow:none;">
                </div>
                </div>
            </div>
            <div style="position:absolute; top:32px; right:10px; width:325px; bottom: 10px; border: 1px solid rgba(0,0,0, 0.2); ">
                <div id="details" class="details" style="position:absolute; top:0px; left:0px; right:0px; bottom: 30px; overflow:hidden;">
                </div>
                <div id="plots" class="details" style="display:none; position:absolute; top:0px; left:0px; right:0px; bottom: 30px; overflow:hidden;">
                </div>
                <div id="hexbin" class="details" style="display:none; position:absolute; top:0px; left:0px; right:0px; bottom: 30px; overflow:hidden;">
                </div>
                <div id="boxplot" class="details" style="display:none; position:absolute; top:0px; left:0px; right:0px; bottom: 30px; overflow:hidden;">
                </div>
                <div id="hist" class="details" style="display:none; position:absolute; top:0px; left:0px; right:0px; bottom: 30px; overflow:hidden;">
                </div>
  
                <div id="selection" style="position: absolute; bottom:20px; height:12px; width:100%; overflow:hide; border-bottom: 1px solid rgba(0,0,0, 0.05); opacity:0.8;">
                    <div id="views" style="display: block; font-size:32px; width:90px; height:10px; overflow:hide; margin-left:auto; margin-right:auto; margin-top:4px;">
                        <a id="listview" class="menu-item" style="color:rgba(0,0,0,1.0)">&#8226;</a>
                        <a id="scatterplotview" class="menu-item" style="color:rgba(110,110,110,1.0)">&#8226;</a>
                        <a id="hexplotview" class="menu-item" style="color:rgba(110,110,110,1.0)">&#8226;</a>
                        <a id="boxplotview" class="menu-item" style="color:rgba(110,110,110,1.0)">&#8226;</a>
                        <a id="histplotview" class="menu-item" style="color:rgba(110,110,110,1.0)">&#8226;</a>
                    </div>
                </div>
            </div>    

        </div>    
    </body>

</html>

</html>
"""

def js_print(browser, lang, event, msg):
    browser.ExecuteFunction("js_print", lang, event, msg)

def html_to_data_uri(html):
    html = html.encode("utf-8", "replace")
    b64 = base64.b64encode(html).decode("utf-8", "replace")
    ret = "data:text/html;base64,{data}".format(data=b64)
    return ret

def scatter_plot(data, labels, x_axis, y_axis, row):
    x = []
    y = []
    s = []
    c = []

    matplotlib.use('Agg')
    
    plt.rc('font', size=6)

    for i in range(len(data)):

        if len(data[i][x_axis]) > 0 and len(data[i][y_axis]) > 0:
            x.append(float(data[i][x_axis]))
            y.append(float(data[i][y_axis]))
            s.append(4)
            c.append('gainsboro')
            
    fig, ax = plt.subplots()

    ax.set_xlabel(labels[x_axis])
    ax.set_ylabel(labels[y_axis])

    ax.yaxis.set_label_position("right")
    fig.set_figwidth(3)
    fig.set_figheight(3)  

    ax.scatter(x, y, s=s, c=c)
    s = []
    s.append(8)

    if len(data[int(row)][x_axis]) > 0 and len(data[int(row)][y_axis]) > 0:
        ax.scatter(float(data[int(row)][x_axis]), float(data[int(row)][y_axis]), color='blue', s=s)
    
    pic_IObytes = io.BytesIO()
    plt.savefig(pic_IObytes, format='png')
    
    plt.close()

    pic_IObytes.seek(0)
    pic_b64 = base64.b64encode(pic_IObytes.read())   

    return pic_b64.decode('utf-8')

def hexbin_plot(data, labels, x_axis, y_axis, row):
    x = []
    y = []
    s = []
    c = []

    matplotlib.use('Agg')
    plt.rc('font', size=6)

    for i in range(len(data)):

        if len(data[i][x_axis]) > 0 and len(data[i][y_axis]) > 0:
            x.append(float(data[i][x_axis]))
            y.append(float(data[i][y_axis]))
           
    fig, ax = plt.subplots()

    ax.set_xlabel(labels[x_axis])
    ax.set_ylabel(labels[y_axis])

    ax.yaxis.set_label_position("right")
    
    fig.set_figwidth(3)
    fig.set_figheight(3)  

    ax.hexbin(x, y, gridsize=20, cmap='binary')

    s = []
    s.append(32)

    if len(data[int(row)][x_axis]) > 0 and len(data[int(row)][y_axis]) > 0:
        ax.scatter(float(data[int(row)][x_axis]), float(data[int(row)][y_axis]), color='blue', s=s)
    
    pic_IObytes = io.BytesIO()
    plt.savefig(pic_IObytes, format='png')
    
    plt.close()

    pic_IObytes.seek(0)
    pic_b64 = base64.b64encode(pic_IObytes.read())   

    return pic_b64.decode('utf-8')

def boxplot_plot(data, labels, column, row):
    x = []
    s = []
    c = []

    matplotlib.use('Agg')
    plt.rc('font', size=6)

    for i in range(len(data)):
        if len(data[i][column]) > 0:
            x.append(float(data[i][column]))
           
    fig, ax = plt.subplots()

    ax.set_ylabel(labels[column])

    ax.yaxis.set_label_position("right")
    
    fig.set_figwidth(3)
    fig.set_figheight(3)  

    ax.boxplot(x)
    ax.set(xticklabels=[])

    s = []
    s.append(32)

    if len(data[int(row)][column]) > 0:
        ax.scatter(1, float(data[int(row)][column]), color='blue', s=s)

    pic_IObytes = io.BytesIO()
    plt.savefig(pic_IObytes, format='png')
    
    plt.close()

    pic_IObytes.seek(0)
    pic_b64 = base64.b64encode(pic_IObytes.read())   

    return pic_b64.decode('utf-8')

def hist_plot(data, labels, column, row):
    x = []
    s = []
    c = []

    matplotlib.use('Agg')
    plt.rc('font', size=6)

    for i in range(len(data)):
        if len(data[i][column]) > 0:
            x.append(float(data[i][column]))
           
    fig, ax = plt.subplots()

    ax.set_ylabel(labels[column])

    ax.yaxis.set_label_position("right")
    
    fig.set_figwidth(3)
    fig.set_figheight(3)  

    n, bins, patches = ax.hist(x, bins=8, color='gainsboro', ec="black")

    bin = 0

    while bin < len(bins) - 1:

        if bins[bin] > float(data[int(row)][column]):
            break

        bin = bin + 1

    patches[bin].set_color('grey')
    patches[bin].set_ec('black')

    pic_IObytes = io.BytesIO()
    plt.savefig(pic_IObytes, format='png')
    
    plt.close()

    pic_IObytes.seek(0)
    pic_b64 = base64.b64encode(pic_IObytes.read())   

    return pic_b64.decode('utf-8')

def main():

    WIDTH = 1300    
    HEIGHT = 840

    cef.Initialize({
        'context_menu' : {
            'enabled': False
        }
    })
    
    window_info = cef.WindowInfo()
    parent_handle = 0

    browser = cef.CreateBrowserSync(url=html_to_data_uri(HTML_code),
                                    window_info=window_info,
                                    window_title="Prattle")

    bindings = cef.JavascriptBindings()
    bindings.SetFunction("process_file", process_file)
    bindings.SetFunction("show_plot", show_plot)
    bindings.SetFunction("show_hexbin", show_hexbin)
    bindings.SetFunction("show_boxplot", show_boxplot)
    bindings.SetFunction("show_hist", show_hist)

    browser.SetJavascriptBindings(bindings)
    cef.MessageLoop()
    del browser
    cef.Shutdown()

def process_file(value, js_callback):    
    f = StringIO(value)
    reader = csv.reader(f, delimiter=',')

    columns = None
    rows = []
    types = []

    for row in reader:
        if columns == None:
            columns = row

            for column in columns:
                types.append("number")

        else:
            rows.append(row)
            
            column = 0

            for cell in row:
                if len(cell) != 0:
                    if cell.isnumeric() or cell.replace('.', '', 1).isnumeric() : 
                        if  types[column] != "string":
                            types[column] = "number"
                    else:
                        types[column] = "string"

                column = column + 1        

    output = {
        'columns' : columns,
        'types' : types,
        'rows' : rows
    }

    js_callback.Call(json.dumps(output))

def show_plot(value, js_callback):  
    plots = []
    continuous = []

    data = json.loads(value)
    types = data['types']    
    row = data['row']

    column = 0

    for datatype in types:
        if datatype == 'number':
            continuous.append(column)
    
        column = column + 1

    while len(continuous) > 1:
        x_axis = continuous.pop(0)

        for y_axis in continuous: 
                plots.append({
                        'x': data['types'][x_axis],
                        'y': data['types'][y_axis],
                        'plot': scatter_plot(data['data'], data['columns'], x_axis, y_axis, row),
                        })
    
    return js_callback.Call(json.dumps(plots))

def show_hexbin(value, js_callback):  

    plots = []
    continuous = []

    data = json.loads(value)
    types = data['types']    
    row = data['row']

    column = 0

    for datatype in types:
        if datatype == 'number':
            continuous.append(column)
    
        column = column + 1

    while len(continuous) > 1:
        x_axis = continuous.pop(0)

        for y_axis in continuous: 
                plots.append({
                        'x': data['types'][x_axis],
                        'y': data['types'][y_axis],
                        'plot': hexbin_plot(data['data'], data['columns'], x_axis, y_axis, row),
                        })
    
    return js_callback.Call(json.dumps(plots))

def show_boxplot(value, js_callback):  
    plots = []
    continuous = []

    data = json.loads(value)
    types = data['types']    
    row = data['row']

    column = 0

    for datatype in types:
        if datatype == 'number':
            continuous.append(column)
    
        column = column + 1

    while len(continuous) > 1:
        x_axis = continuous.pop(0)

        plots.append({
                'x': data['types'][x_axis],
                'plot': boxplot_plot(data['data'], data['columns'], x_axis, row),
                })
    
    return js_callback.Call(json.dumps(plots))

def show_hist(value, js_callback):  
    plots = []
    continuous = []

    data = json.loads(value)
    types = data['types']    
    row = data['row']

    column = 0

    for datatype in types:
        if datatype == 'number':
            continuous.append(column)
    
        column = column + 1

    while len(continuous) > 1:
        x_axis = continuous.pop(0)

        plots.append({
                'x': data['types'][x_axis],
                'plot': hist_plot(data['data'], data['columns'], x_axis, row),
                })

    return js_callback.Call(json.dumps(plots))

if __name__ == '__main__':
    main()