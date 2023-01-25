import React from 'react'
import axios from '../config/axios'

const UseFetch = (path) => {

    const [data, setData] = React.useState(null)
    const [error, setError] = React.useState(null)
    const [loading, setLoading] = React.useState(false)

    const trigger = React.useRef(true)

    React.useEffect(() => {

        if (trigger) {
            axios.get(path ?? "/").then((result) => {
                setData(result.data)
                setLoading(false)
            }).catch((errorResult) => {
                setError(errorResult)
                setLoading(false)
            })
        }


        return () => {
            trigger.current = false
        }

    }, [path])

    return { data, error, loading }
}

export default UseFetch