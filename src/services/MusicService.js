import { musicURL } from "@/helpers/URLHelper"
//import { getToken } from "@/helpers/CookieHelper"

/**
 * 
 * @param {*} username 
 */
function getMusic(username){
    return fetch(musicURL+username, {
        method: "GET",
        headers: new Headers({
            // 'Authorization': 'Bearer ' + getToken(),
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    }).then(res => {
        if (res.ok){
            return Promise.resolve(res.json())
        } else {
            return Promise.reject(new Error(res.json()))
        }
    })
}

export const MusicService = {
    getMusic
}

