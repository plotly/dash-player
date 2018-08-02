import React, {Component} from 'react';
import {Player} from '../src';

class Demo extends Component {
    constructor() {
        super();
        this.state = {
            value: ''
        }
    }

    render() {
        return (
            <div>
                <h1>dash-player Demo</h1>

                <hr/>
                <h2>Player</h2>
                <Player />
                <hr/>
            </div>
        );
    }
}

export default Demo;
