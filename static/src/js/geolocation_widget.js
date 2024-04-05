/** @odoo-module **/
import { registry } from "@web/core/registry";
import { useInputField } from "@web/views/fields/input_field_hook";
import { _t } from "web.core";
const { Component, useRef, onMounted } = owl;

export class GeoLocationField extends Component {
    static template = 'GeoLocationField';

    setup() {
        super.setup();
        this.inputRef = useRef('geoInput');
        onMounted(() => {
            this._getCurrentLocation();
            this.inputRef.el.addEventListener('click', this._openGoogleMaps.bind(this));
        });
    }

    async _getCurrentLocation() {
        try {
            const position = await this._getCurrentPosition();
            const { latitude, longitude } = position.coords;
            this.inputRef.el.value = `${latitude},${longitude}`;
            this.props.update(this.inputRef.el.value);
        } catch (error) {
            console.error('Error getting current location:', error);
        }
    }

    _getCurrentPosition() {
        return new Promise((resolve, reject) => {
            navigator.geolocation.getCurrentPosition(
                position => resolve(position),
                error => reject(error)
            );
        });
    }

    _openGoogleMaps() {
        const location = this.inputRef.el.value;
        if (location) {
            const url = `https://www.google.com/maps/search/?api=1&query=${location}`;
            window.open(url, '_blank');
        }
    }
}

GeoLocationField.components = { useRef };
registry.category("fields").add("geo_location", GeoLocationField);
