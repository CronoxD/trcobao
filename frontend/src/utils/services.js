

import { getToken, URL_API } from "./index";

class Service {
	constructor() {
		this.url = URL_API
		this.token = getToken()

		this.settings = {
			method: 'GET', //DEFAULT GET
			credentials: 'include',
			headers: {
				'X-CSRFToken': this.token
			}
		}
	}

	get(path) {
		return fetch(this.url + path, { credentials: 'include' })
			.then(resp => resp.json())
			.then(res => res)
			.catch(() => 'No existe el elemeno')
	}

	post(path, payload) {
		this.settings.method = 'POST'
		return this.interSend(path, payload)
	}

	put(path, payload) {
		this.settings.method = 'PUT'
		return this.interSend(path, payload)
		
	}

	interSend(path, payload) {
		this.settings.body = JSON.stringify(payload)

		return fetch(this.url + path, this.settings)
			.then(resp => resp.json())
			.then(res => res)
	}
}

export default Service