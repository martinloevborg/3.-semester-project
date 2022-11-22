import { loginURL } from "@/helpers/URLHelper"
//import { getToken } from "@/helpers/CookieHelper"

/**
 * 
 * @param {*} jsonUser 
 */
function login(jsonUser){
    return fetch(loginURL, {
        method: "POST",
        headers: new Headers({
            // 'Authorization': 'Bearer ' + getToken(),
            'Content-Type': 'application/json'
        }),
        body: jsonUser
    }).then(res => {
        if (res.ok){
            alert("200")
            return Promise.resolve(res.json())
        } else {
            alert("400")
            return Promise.reject(new Error(res.json()))
        }
    })
}
export const LoginService = {
    login
}