class InstaGram{
    constructor(instaUserName, fullName){
        this.instaUserName = instaUserName
        this.fullName = fullName
        this.followers = 0
        this.following = 0
    }
    
    follow = (user) => {
        user.followers ++
        this.following ++
    }
}

const user1 = new InstaGram("trishan_wagle", "Trishan Wagle")
const user2 = new InstaGram("smarika9", "Smarika")  
console.log(user1.instaUserName, user1.fullName)

user1.follow(user2)
console.log(user1.followers, user1.following)
console.log(user2.followers, user2.following)