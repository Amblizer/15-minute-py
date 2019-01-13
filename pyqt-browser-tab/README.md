
## Credit

Inspired by [browser_tabbed][c1]

[c1]: https://github.com/mfitzp/15-minute-apps/tree/master/browser_tabbed

## Function

1. Webview window.
1. Navigation bar and address bar.
1. Tab bar for multi-view.

## Configuration

1. PyQt > 5.6

    `conda install -c defaults pyqt=5 qt`

## Keypoints

1. Navigation bar covered by system title bar.

    Method 1: disable system title bar by `self.setWindowFlags(QtCore.Qt.FramelessWindowHint)`.

1. Contents blur.
