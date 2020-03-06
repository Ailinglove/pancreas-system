    function showDetails(row){
      this.patientID=row.fields.patientID
      this.houspitalID=row.fields.houspitalID
      this.$router.push({name:'detailInfo',params:{patientID:this.patientID,
          houspiatlID:this.houspitalID}})

    }

    export {
  showDetails
    }
