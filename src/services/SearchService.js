import { musicURL } from "@/helpers/URLHelper"
//import { getToken } from "@/helpers/CookieHelper"

/**
 * 
 * @param {*} songName 
 */
function getMusicSearch(songName){
    return fetch(musicURL+songName, {
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

export const SearchService = {
    getMusicSearch
}
