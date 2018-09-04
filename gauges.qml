import QtQuick 2.7
import QtQuick.Extras 1.4

Image {
    id: image
    x: 0
    y: 0
    width: 800
    height: 480
    source: "graphics/revero_800.png"

    CircularGauge {
        id: rpmGauge
        objectName: "rpmGauge"
        x: 392
        y: 268
        width: 180
        height: 180
        value: 10

        Text {
            id: text1
            x: 71
            y: 43
            color: "#ffffff"
            text: qsTr("RPM")
            renderType: Text.NativeRendering
            lineHeight: 1
            horizontalAlignment: Text.AlignHCenter
            font.pixelSize: 20
        }

        Text {
            id: text2
            x: 263
            y: 43
            color: "#ffffff"
            text: qsTr("Torque")
            lineHeight: 1
            font.pixelSize: 20
            renderType: Text.NativeRendering
            horizontalAlignment: Text.AlignHCenter
        }
    }

    CircularGauge {
        id: torqueGauge
        objectName: "torqueGauge"
        x: 598
        y: 267
        width: 180
        height: 180
        value: 10
    }


}




