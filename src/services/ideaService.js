import api from "@/services/api"
export default {
  async checkIdeaScore(payload) {
    if (!payload.inputString || !payload.ideaText) {
      return Promise.reject("Input string and idea text is requred")
    }
    let formdata = new FormData()
    formdata.append("input_string", payload.inputString)
    formdata.append("idea_text", payload.ideaText)
    formdata.append("round", payload.round)
    let ideaList = null
    await api.post(`getIdeaScore/`, formdata).then((response) => {
      const status = response.data.status
      if (status == "success") {
        ideaList = response.data.idea_list
      }
    })
    return ideaList
  },
  async checkRoundInfo() {
    let roundInfo = null
    await api.get(`getTestingInfo/`).then((response) => {
      roundInfo = response.data
    })
    return roundInfo
  },
  async getObjectKey(payload) {
    let formdata = new FormData()
    formdata.append("round", payload.round)
    let objectKey = ""
    await api.post(`getObjectKey/`, formdata).then((response) => {
      objectKey = response.data.object_key
    })
    return objectKey
  },
  async getNextKey(payload) {
    let formdata = new FormData()
    formdata.append("object_index", payload.objectIndex)
    let objectKey = ""
    await api.post(`getNextKey/`, formdata).then((response) => {
      objectKey = response.data.object_key
    })
    return objectKey
  },
  async getIdeaList() {
    let ideaList = null
    let formdata = new FormData()
    formdata.append("round", 2)
    await api.post(`getIdeaList/`, formdata).then((response) => {
      ideaList = response.data.idea_list
    })
    return ideaList
  },
  async setUserRound(payload) {
    let formdata = new FormData()
    formdata.append("round", payload.round)
    await api.post(`setUserRound/`, formdata).then((response) => {
      console.log(response)
    })
  },
  async getScoreList() {
    let scoreList = null
    let formdata = new FormData()
    formdata.append("round", 2)
    await api.post(`getScoreList/`, formdata).then((response) => {
      scoreList = response.data.score_list
    })
    return scoreList
  },
}
